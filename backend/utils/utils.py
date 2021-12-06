import os
import six
# from google.cloud import storage
from json import loads, dumps
from os import environ
from starlette.responses import JSONResponse
from starlette.requests import Request
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr
from typing import List
from fastapi_mail.email_utils import DefaultChecker
from datetime import date
from ..settings import get_settings

settings = get_settings()

# def get_base64_encoded_image(image_path):
#     with open(image_path, "rb") as img_file:
#         img_bytes = base64.b64encode(img_file.read()).decode('utf-8')
#         return str(img_bytes)


class FlaskMailMailJet:
    MAIL_USE_SSL = True#This works: MAIL_USE_TLS no worky
    MAIL_SERVER = 'in-v3.mailjet.com'

    # Skystone Acct
    MAIL_USERNAME = environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD')
    MAIL_PORT = environ.get('MAIL_PORT', 465)
    MAIL_DEFAULT_SENDER = 'alexjslessor@gmail.com'

    


class Utils:

    def html_email(items):
        checkout_html_email = f""" <p>Hello, thank's for your order. You will be invoiced once your order has shipped.</p> <ul> {items} </ul>  """
        return checkout_html_email

    conf = ConnectionConfig(MAIL_USERNAME=FlaskMailMailJet.MAIL_USERNAME, 
                            MAIL_PASSWORD = FlaskMailMailJet.MAIL_PASSWORD, 
                            MAIL_FROM = FlaskMailMailJet.MAIL_DEFAULT_SENDER, 
                            MAIL_PORT = FlaskMailMailJet.MAIL_PORT, 
                            MAIL_SERVER = FlaskMailMailJet.MAIL_SERVER, 
                            MAIL_FROM_NAME='Commercial Oil Order Confirmation.', 
                            MAIL_TLS=False, 
                            MAIL_SSL=True)

    stat_code = {
        'stage_1': 'Pending',
        'stage_2': 'Acknowledged',
        'stage_3': 'In Production',
        'stage_4': 'Shipped',
        'stage_5': 'Complete',
        'cancelled': 'Cancelled',
        'backordered': 'Back-Ordered'}


    def query_to_json(query):
        q = query.to_json()
        return loads(q)
        
    def stripe_to_json(data):
        a = dumps(data)
        return loads(a)


    def get_last_invoice_number(mongo_model):
        invoice_num = None
        try:
            # Search orders by most recent invoice # and append 1 to create new inv
            _order_count = mongo_model.objects.only('invoice_num').order_by('-invoice_num').first()
            order_count = int(_order_count.invoice_num) + 1
            invoice_num = str(order_count)
        except Exception:
            # only required for the first time db is created.
            invoice_num = str(1000000)
        return invoice_num



class DocTemplates:

  def commercial_invoice_template(self, 
                                  from_email, 
                                  from_name, 
                                  from_street, 
                                  to_name, 
                                  to_street, 
                                  invoice_number, 
                                  todays_date, 
                                  item_table, 
                                  total_price):
      return f'''<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Invoice</title>
        <meta name="description" content="Invoice - Commercial Oil">
        <meta name="author" content="Commercial Invoice">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    </head>
    
    <body>
      <div class="container invoice">
      
        <div class="invoice-header">
        
          <div class="row">
          
            <div class="col-8">
              <h5><small> Commercial Invoice </small></h5>
              <h6 class="text-muted">Export Date: {todays_date}</h6>
              <h6 class="text-muted">Export Ref: {invoice_number}</h6>
            </div>
            
            <div class="col-4">
              <div class="media">
              
                <div class="media">
                  <img class="mr-3 logo" src="https://dummyimage.com/70x70/000/fff&text=ACME" />
                </div>
                
                <ul class="media-body list-unstyled">
                  <li><strong>{ from_name }</strong></li>
                  <li>{ from_street }</li>
                  <li>{ todays_date }</li>
                  <li>{ from_email }</li>
                </ul>
                
              </div>
            </div>
            
          </div>
        </div>
        

        <div class="invoice-body">
    <div class="row justify-content-between">

        <div class='col-6'>
            <div class="card text-left mr-3">
                <div class="card-header">
                { from_name }
                </div>
                <div class='card-body'>
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item">Country of Export: Canada</li>
                        <li class="list-group-item">Country of Manufacture: Canada</li>
                        <li class="list-group-item">Country of Ultimate Destionation: U.S.A.</li>
                    </ul>
                </div>
            </div>
        </div>
        
        <div class='col-6'>
            <div class="card text-left">
                <div class="card-header">
                { to_name }
                </div>
                <div class='card-body'>
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item">Cras justo odio</li>
                        <li class="list-group-item">Dapibus ac facilisis in</li>
                        <li class="list-group-item">Vestibulum at eros</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

 </div>
          
           {item_table}

    <table id="total">
      <thead>
        <th>Terms</th>
        <th>Account</th>
        <th>Total due</th>
      </thead>
      <tbody>
        <tr>
          <td>45 Days</td>
          <td>NHOU</td>
          <td>{ total_price }</td>
        </tr>
      </tbody>
    </table>
    
     </body>
    </html>'''

  def invoice_template(self, 
                       from_name, 
                       from_street, 
                       to_name, 
                       to_street, 
                       invoice_number, 
                       todays_date, 
                       item_table, 
                       total_price):
    return f"""<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Invoice</title>
        <meta name="description" content="Invoice - Commercial Oil">
        <meta name="author" content="Author">
    </head>

    <body>
        <h1>Invoice</h1>
        
    <aside>
      <address id="from">
        { from_name }
        { from_street }
      </address>

      <address id="to">
        { to_name }
        {to_street}
      </address>
    </aside>

    <dl id="informations">
      <dt>Invoice</dt>
      <dd>{ invoice_number }</dd>
      <dt>Date</dt>
      <dd>{ todays_date }</dd>
    </dl>
    
        {item_table}
        
    <table id="total">
      <thead>
        <th>Terms</th>
        <th>Account</th>
        <th>Total due</th>
      </thead>
      <tbody>
        <tr>
          <td>45 Days</td>
          <td>NHOU</td>
          <td>{ total_price }</td>
        </tr>
      </tbody>
    </table>
    
      </body>
    </html>
    """