import McButton from './components/McButton'
import './style.css'

export { McButton }

export default {
  install(app: any) {
    app.component('McButton', McButton)
  },
}
