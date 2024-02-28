module.exports = {
  root: true,
  extends: [
    "eslint:recommended",
    "plugin:vue/recommended",
    "plugin:prettier/recommended"
  ],
  env: {
    browser: true,
    node: true,
  },
  plugins: ["vue"],
  parserOptions: {
    parser: "babel-eslint",
    sourceType: "module",
    allowImportExportEverywhere: false,
    codeFrame: false,
  },

  //  "off" or 0 - 关闭规则
  // "warn" or 1 - 将规则视为一个警告（不会影响退出码）
  // "error" or 2 - 将规则视为一个错误 (退出码为1)
  rules: {
    // 使用prettier格式缩进
    'indent': 0,
    // 强制使用骆驼拼写法命名约定
    'camelcase': [2, {properties: "never"}],
    'semi': [2, 'never'],
    'quotes': [2, 'single', {'avoidEscape': true}],
    // 禁止没使用的变量
    'no-unused-vars': 2,
    // 避免使用不必要的括号(关闭，与prettier冲突)
    'no-extra-parens': 0,
    // 禁用行尾分号
    'no-extra-semi': 2,
    // 禁用行尾空格
    'no-trailing-spaces': 2,
    // 对象中禁止出现重复的key
    'no-dupe-keys': 2,
    // 强制对象赋值引用使用点形式
    'dot-notation': 2,
    // 魔术数字
    'no-magic-numbers': [
      'warn',
      {
        ignoreArrayIndexes: true
      }
    ],
    // 禁止对 String，Number 和 Boolean 使用 new 操作符
    'no-new-wrappers': 2,
    // 自我赋值
    'no-self-assign': 1,
    // 数组使用一致的空格
    'array-bracket-spacing': 1,
    // 强制把变量的使用限制在其定义的作用域范围内
    'block-scoped-var': 2,
    'block-spacing': 2,
    // 强制使用let或const 不能使用var
    'no-var': 2,
    // 要求对象字面量简写语法
    'object-shorthand': 1,
    // 要求构造函数首字母大写 （要求调用 new 操作符时有首字母大小的函数，允许调用首字母大写的函数时没有 new 操作符。）
    'new-cap': [
      2,
      {
        newIsCap: true,
        capIsNew: false
      }
    ],
    // 强制一行的最大长度
    'max-len': [1, 120],
    // 强制 function 块最多允许的的语句数量
    'max-statements': [1, 200],
    // 强制回调函数最大嵌套深度 5层
    'max-nested-callbacks': [1, 5],
    // 控制逗号前后的空格
    'comma-spacing': [
      2,
      {
        before: false,
        after: true
      }
    ],
    'arrow-body-style': 0,
    // 要求箭头函数的参数使用圆括号
    'arrow-parens': [1, 'as-needed'],
    // 禁止重新声明变量
    'no-redeclare': 2,
    // if return之后没必要使用else
    'no-else-return': 1,
    // 禁止使用弱等于
    'eqeqeq': 2,

    'comma-dangle': ['error', 'never'],

    // 花开括号样式
    // 'brace-style': [2, 'tbs'],
    'callback-return': 2,
    'computed-property-spacing': [2, 'never'],
    'dot-location': [2, 'property'],

    // eslint与prettier冲突项
    'vue/html-self-closing': 0,
    "vue/max-attributes-per-line": 0,
    'vue/attribute-hyphenation': 0,
    'vue/require-default-prop': 0,
    "vue/singleline-html-element-content-newline": 0,
    "vue/multiline-html-element-content-newline":0,

    'prettier/prettier': 2,
  },

  // 全局变量
  globals: {
    WebViewJavascriptBridge: true,
    reject: true,
    resolve: true
  },
};
