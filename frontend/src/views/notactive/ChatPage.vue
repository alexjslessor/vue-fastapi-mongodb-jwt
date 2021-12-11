<template>
  <div>
    <p id="connectMessage"></p>
    <!-- <v-form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </v-form>
        <ul id='messages'>
        </ul> -->
    <v-container fluid>
      <v-row>
        <v-col cols="12" md="6" class="mx-auto">
          <!-- <v-form @keyup.native.enter="sendMessage"> -->
          <v-form @submit.prevent="sendMessage()">
            <v-textarea
              solo
              name="input-7-1"
              label="Begin Chat..."
              v-model="sentMsg"
              hint="Hint text"
            >
            </v-textarea>

            <v-btn type="submit">Submit</v-btn>
          </v-form>
        </v-col>

        <v-col>
          <v-card class="mx-auto" max-width="400">
            <v-list id="messages"> </v-list>
            <!-- <v-list-item v-for='(i, idx) in received_message' :key='idx'> -->
            <!-- <v-list-item> -->
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
  <script>
const connection = new WebSocket("ws://localhost:5000/ws");
// import io from "socket.io-client";
// const socket = io("ws://localhost:5000/ws");
export default {
  data() {
    return {
      connectMessage: "",
      // connection: new WebSocket("ws://localhost:5000/ws"),
      sentMsg: "",
    };
  },

  methods: {
    sendMessage() {
      console.log("sent --- sendMessage: ");
      connection.send(this.sentMsg);
      this.sentMsg = '';
    },

    receiveMessage() {
      connection.onmessage = function (event) {
        console.log("received --- onmessage: ", event.data);
        let messages = document.getElementById("messages");

        let message = document.createElement("li");
        messages.appendChild(message);

        let content = document.createTextNode(event.data);
        message.appendChild(content);
      };
    },

    getCon() {
      connection.onopen = function (event) {
        // this.connectMessage = 'Connected to Chat.'
        console.log("Successfully connected to the echo websocket server...");

        let success = document.getElementById("connectMessage");
        let content = document.createTextNode("Successfully Connected!");
        success.appendChild(content);
      };
    },
  },

  mounted() {
    this.receiveMessage();
  },
  
  created() {
    this.getCon();
    // let success = document.getElementById('connectMessage')
    // let content = document.createTextNode('Success')
    // success.appendChild(content)
  },
};
</script>
// getChat() {
    //     // const ws = new WebSocket("ws://localhost:5000/ws");
    //         ws.onmessage = function(event) {
    //             let messages = document.getElementById('messages')
    //             let message = document.createElement('li')
    //             let content = document.createTextNode(event.data)
    //             message.appendChild(content)
    //             messages.appendChild(message)
    //         };

    //         function sendMessage(event) {
    //             let input = document.getElementById("messageText")
    //             ws.send(input.value)
    //             input.value = ''
    //             event.preventDefault()
    //         }
    //     }

    // }
  
  