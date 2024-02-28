import orderApis from "./orderApis";
import customerApis from "./customerApis";
import stepApis from "./stepApis";
import staffApis from "./staffApis";
import adminApis from "./adminApis";

export default {
  ...orderApis,
  ...customerApis,
  ...stepApis,
  ...staffApis,
  ...adminApis,
} as {
  [key: string]: string;
};
