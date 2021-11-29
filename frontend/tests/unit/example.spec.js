import { shallowMount } from '@vue/test-utils'
// import HelloWorld from '@/components/HelloWorld.vue'
import pageTitle from '@/components/fragments/pageTitle.vue';

// cd frontend
// yarn test:unit
// https://www.digitalocean.com/community/tutorials/vuejs-testing-vue-with-jest
describe('pageTitle.vue', () => {
  it('renders props.msg when passed', () => {
    // this must be same as what you name your prop in component
    const titleText = 'NHW-55'
    const wrapper = shallowMount(pageTitle, {
      propsData: { titleText }
    })
    expect(wrapper.text()).toMatch(titleText)
  })
})

