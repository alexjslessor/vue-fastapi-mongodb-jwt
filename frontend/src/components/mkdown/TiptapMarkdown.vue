<template>
    <node-view-wrapper class="code-block">

      <pre><node-view-content as="code" /></pre>

    </node-view-wrapper>
</template>
<script>
import { NodeViewWrapper, NodeViewContent, nodeViewProps } from '@tiptap/vue-2'
// import { Editor, EditorContent, VueNodeViewRenderer } from '@tiptap/vue-2'
// import Document from '@tiptap/extension-document'
// import Paragraph from '@tiptap/extension-paragraph'
// import Text from '@tiptap/extension-text'
// import CodeBlockLowlight from '@tiptap/extension-code-block-lowlight'
// import lowlight from 'lowlight'

export default {
    components: { NodeViewWrapper, NodeViewContent },
    
    props: nodeViewProps,

    data() {
      return {
        languages: this.extension.options.lowlight.listLanguages(),
        editor: null,
      }
    },
  
    computed: {
      selectedLanguage: {
        get() {
          return this.node.attrs.language
        },
        set(language) {
          this.updateAttributes({ language })
        },
      },
    },

    mounted() {
    this.editor = new Editor({
      extensions: [
        Document,
        Paragraph,
        Text,
        CodeBlockLowlight
          .extend({
            addNodeView() {
              return VueNodeViewRenderer(TiptapMarkdown)
            },
          })
          .configure({ lowlight }),
      ],
      content: ``,
    })
  },

  beforeDestroy() {
    this.editor.destroy()
  },

  }
  </script>

<!-- <style scoped>
    .code-block {
        position: relative;    
    }

    .code-block select {
      position: absolute;
      top: 0.5rem;
      right: 0.5rem;
    }    
</style> -->
  <!-- <style lang="scss" scoped>
  .code-block {
    position: relative;
  
    select {
      position: absolute;
      top: 0.5rem;
      right: 0.5rem;
    }
  }
  </style> -->