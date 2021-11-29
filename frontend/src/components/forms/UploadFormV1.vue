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
          class="text-none font-weight-medium"
          style='color:#D92231;'
          round
          depressed
          :loading="isSelecting"
          @click="onButtonClick">
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
          @change="onFileChanged">
      </div>
</template>
<!-- <v-file-input show-size label="File input" @change="uploadImages"></v-file-input> -->
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
        uploadImage(event) {
            // console.log('event:  ', event);
            // console.log('sku: ', this.sku);
            // console.log('form sku:  ', this.productSku)
            const e = {event: event, sku: this.sku};
            return this.uploadImages(e);
        },
        onButtonClick() {
            this.isSelecting = true
            window.addEventListener('focus', () => {
              this.isSelecting = false
            }, { once: true })
            this.$refs.uploader.click()
        },
        onFileChanged(e) {
            const e = {event: event, sku: this.sku};
            return this.uploadImages(e);
        //   this.selectedFile = e.target.files[0]
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