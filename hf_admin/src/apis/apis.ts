import orderApis from "./orderApis"
import customerApis from "./customerApis"
import stepApis from "./stepApis"

export default {
  ...orderApis,
  ...customerApis,
  ...stepApis,
} as {
  [key: string]: string
}
