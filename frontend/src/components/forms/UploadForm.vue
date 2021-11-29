<template>
    <!-- <div class='dropper'>
      <input type="file"
             accept='image/*'
             @change='uploadImage($event.target.files)' />
        <span>Upload here</span>
    </div> -->

    <div>
        <v-btn
          color="primary"
          class="text-none"
          style='color:#D92231;'
          rounded
          depressed
          :loading="isSelecting"
          @click="onButtonClick"
        >
          <v-icon left>
            mdi-cloud-upload
          </v-icon>
          {{ buttonText }}
        </v-btn>
        <input
          ref="uploader"
          class="d-none"
          type="file"
          accept="image/*"
          @change="onFileChanged($event.target.files)" />
      </div>
</template>
<script>
import { mapActions } from "vuex";
export default {
    name: 'UploadForm',
    props: ['productSku'],
    components: {},
    data() {
      return {
          sku: this.productSku,

          defaultButtonText: 'Upload Image',
          selectedFile: null,
          isSelecting: false
        //   defaultButtonText: '画像をアップロード',

      };
    },

    computed: {
        buttonText() {
            return this.selectedFile ? this.selectedFile.name : this.defaultButtonText
        }
    },

    methods: {
        ...mapActions(['uploadImages']),
        // uploadImage(event) {
            // const e = {event: event, sku: this.sku};
            // return this.uploadImages(e);
        // },
        onButtonClick() {
            this.isSelecting = true
            window.addEventListener('focus', () => {
              this.isSelecting = false
            }, { once: true })
            this.$refs.uploader.click()
        },

        onFileChanged(event) {
            // this.selectedFile = event
        //   this.selectedFile = event.target.files[0]
          const e = {event: event, sku: this.sku};
          return this.uploadImages(e);
        }
    }
}
</script>
<style scoped>
.v-icon--left {
  margin-right: 8px;
}

.dropper {
    height: 30vh;
    /* width: 50%; */
    border:  2bx dash black;
    border-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
}
.dropper:hover {
    background-color: #eee;

}

input {
    width: 30%;
    height: 30vh;
    position: absolute;
    opacity: 0;
}

</style>