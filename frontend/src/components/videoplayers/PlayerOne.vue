<template>
  <div>
    <!-- <card>
        <video width="320" height="240" ref="videoPlayer">
          <source
            src="https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4"
            type="video/mp4"
          />
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

    <v-container fluid class="">
      <v-layout column wrap>
        <v-flex xs12 sm6 md6 lg6 xl6 class="mx-auto">
          <v-card elevation="5" class="mt-3" color="rgba(0, 0, 0, 0)">
            <!-- <v-app-bar flat color="rgba(0, 0, 0, 0)"> -->

            <video ref="videoPlayer" max-height="100px" max-width="100px">
              <!-- <source
                src="https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4"
                type="video/mp4"/> -->
              <source
                src="https://storage.googleapis.com/comoil-fastapi/nhou_video/Mororhead%20Garage%20Customer%20Testimonial-Fe9Bk789014.mp4"
                type="video/mp4"
              />
              Your browser does not support the video tag.
            </video>
            <!-- </v-app-bar> -->

            <!-- <v-card-actions class=''>
          <v-list-item three-line style="position: relative;">
            <v-list-item-icon>
              <v-btn @click="play">
                <v-icon color='secondary'>mdi-play</v-icon>
              </v-btn>
            </v-list-item-icon>

            <v-list-item-icon>
              <v-btn @click="pause">
                <v-icon color='secondary'>mdi-pause</v-icon>
              </v-btn>
            </v-list-item-icon>

            <v-list-item-icon>
              <v-btn @click="setSpeed(1.5)">
                <v-icon color='secondary'>mdi-speedometer</v-icon>
              </v-btn>
            </v-list-item-icon>
          </v-list-item>
        </v-card-actions> -->

            <v-row class="">
              <v-card-actions class="mx-auto" justify="center">
                <div classs="my-4 ">
                  <v-btn bottom icon @click="play">
                    <v-icon color="secondary">mdi-play</v-icon>
                  </v-btn>

                  <v-btn icon @click="pause">
                    <v-icon color="secondary">mdi-pause</v-icon>
                  </v-btn>

                  <v-btn icon @click="stop">
                    <v-icon color="secondary">mdi-stop</v-icon>
                  </v-btn>

                  <v-btn icon @click="setSpeed(0.5)">
                    <v-icon color="secondary">mdi-speedometer-slow</v-icon>
                  </v-btn>

                  <v-btn icon @click="setSpeed(1)">
                    <v-icon color="secondary">mdi-speedometer-medium</v-icon>
                  </v-btn>

                  <v-btn icon @click="setSpeed(1.5)">
                    <v-icon color="secondary">mdi-speedometer</v-icon>
                  </v-btn>
                </div>
              </v-card-actions>
            </v-row>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>
  
  <script>
export default {
  methods: {
    play() {
      this.$refs.videoPlayer.play();
    },
    pause() {
      this.$refs.videoPlayer.pause();
    },
    stop() {
      const { videoPlayer } = this.$refs;
      videoPlayer.pause();
      videoPlayer.currentTime = 0;
    },
    setSpeed(speed) {
      this.$refs.videoPlayer.playbackRate = speed;
    },
  },
};
</script>
  