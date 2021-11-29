export default {

    qtyShippedColor(qtyOrdered, qtyShipped) {
        if (qtyOrdered == qtyShipped) return 'green'
        else if ( qtyOrdered != qtyShipped ) return 'secondary'
        else return 'blue'
    },
    getColor(item) {
        if (item == 0) return 'green'
        else if (item != 0) return 'secondary'
        else return 'blue'
    },
    colorStatus(item) {
        // if (item == 'In Production') return 'secondary'
        if (item == 'In Production') return 'green'
        else if (item == 'Pending') return 'secondary'
        else if (item == 'Acknowledged') return 'purple'
        else if (item == 'Shipped') return 'green'
        else if (item == 'Complete') return 'green'
        else if (item == 'Cancelled') return 'secondary'
        else return 'pink'
        // else return 'blue'
    },

    //merge these two --. colorBoolean()?
    colorActive(item) {
      if (item == 1) return 'green'
      else return 'secondary'
    },
    colorInventory(item) {
      if (item > 0) return "green";
      else return "secondary";
    },

    floatToFixed(float) {
      return parseFloat(float).toFixed(2);
    },
    formatDate(value) {
      return new Date(value).toISOString().substr(0, 10);
    },
}


