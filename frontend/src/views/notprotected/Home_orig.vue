<template>
  <div>
    <!-- <v-layout row wrap>
      <v-flex xs12 sm12 md12 lg12 xl12 class=''>
        <v-card flat hover elevation="5" class="mx-auto pl-4 pr-4 pb-4" style="color:white">
            <my-chart v-if="loaded" :chartdata="chartdata" 
                      :options='options' label='Death ON'/>
        </v-card>
      </v-flex>
    </v-layout> -->

    <!-- <card>
    <video width="320" height="240" ref="videoPlayer">
      <source
        src="https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4"
        type="video/mp4" />
      Your browser does not support the video tag.
    </video>
    <div>
      <v-btn @click="play">play</v-btn>
      <v-btn @click="pause">pause</v-btn>
      <v-btn @click="stop">stop</v-btn>
      <v-btn @click="setSpeed(0.5)">0.5x</v-btn>
      <v-btn @click="setSpeed(1)">1x</v-btn>
      <v-btn @click="setSpeed(1.5)">1.5x</v-btn>
      <v-btn @click="setSpeed(2)">2x</v-btn>
    </div>
    </card> -->
    <!-- <PlayerOne/> -->
    <!-- <SockIO/> -->
    <!-- <Markdown/> -->

    <home/>
  </div>
</template>
<script>
  // https://github.com/Joabsonlg/vuetify-landing-page/blob/master/src/App.vue
  
// import MyChart from '@/components/charts/MyChart';
// import axios from "axios";
// import PlayerOne from '@/components/videoplayers/PlayerOne';
// import Markdown from '@/components/markDown/Markdown';
// import SockIO from '@/components/SockIO';
// import foote from "./components/Footer";
import home from "@/components/landing/HomeSection";
// import about from "./components/AboutSection";
// import download from "./components/DownloadSection";
// import pricing from "./components/PricingSection";
// import contact from "./components/ContactSection";
export default {
  components: {
    // navigation,
    // foote,
    home,
    // about,
    // download,
    // pricing,
    // contact,
    // PlayerOne,
    // SockIO,
    // Markdown
    // MyChart
  },

  data: () => ({
    chartdata: {},
          shipToData: [],
          queData: [],

          items: [],
          loaded: false,
          options: {
            // type: 'horizontalBar',
              responsive: true,
              maintainAspectRatio: false,
              backgroundColor: 'white',
              scales: {
                  yAxes: [{
                    ticks: {
                      beginAtZero: true
                    },
                    gridLines: {
                      display: true
                    }
                  }],
                  xAxes: [ {
                    gridLines: {
                      display: true
                    }
                  }]
                },
              legend: {
                labels: {
                  // This more specific font property overrides the global property
                  fontColor: '#e2e2e2',
                  defaultFontSize: 16,
                  }
              }

          },
  }),


  // methods: {
  //   play() {
  //     this.$refs.videoPlayer.play();
  //   },
  //   pause() {
  //     this.$refs.videoPlayer.pause();
  //   },
  //   stop() {
  //     const { videoPlayer } = this.$refs;
  //     videoPlayer.pause();
  //     videoPlayer.currentTime = 0;
  //   },
  //   setSpeed(speed) {
  //     this.$refs.videoPlayer.playbackRate = speed;
  //   },
  // },

  // methods: {
  //   async getData() {
  //       const global_url = 'http://localhost:5000';

  //       const url = `${global_url}/stats/death_comparison`;
  //       let data = await axios.get(url, { withCredentials: true });
  //       return data.data;
  //   },
  // },

  // async mounted() {
  //     this.loaded = false
  //     const data = await this.getData();

  //     let qty_ordered = data.map(list => {
  //         return list.VALUE;
  //     });
  //     let skus = data.map(list => {
  //         return list.cause_of_death;
  //     });

    // console.log('Ontario Death Comparison: ', Object.keys(data[0]));

  //   const data_c = {
  //           labels: skus,
  //           // labels: Object.keys(data[0]),
  //           datasets: [
  //                 {
  //                   label: 'Causes of Death in Ontario (2019 Deaths with 2020 COVID Deaths)',
  //                   data: qty_ordered,
  //                   backgroundColor: 'white',
  //                 },
  //                 // {
  //                 //   label: 'Total Filled',
  //                 //   data: qty_filled,
  //                 //   backgroundColor: 'red',
  //                 // }
  //           ]
  //   };
  //   this.chartdata = data_c;
  //   // this.queData = data;
  //   this.loaded = true;
  // },

}
// 1G1JD5EH3C4128582
</script>