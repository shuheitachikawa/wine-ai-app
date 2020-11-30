module.exports = {
  root: true,
  env: {
    browser: true,
    node: true,
  },
  parserOptions: {
    parser: '@typescript-esling/parser',
    ecmaVersion: 2017,
    ecmaFeatures: {
      legacyDecorators: true
    },
    sourceType: 'module',
    project: "./tsconfig.json"
  },
  extends: [
    '@nuxtjs/eslint-config-typescript',
    'prettier',
    'prettier/vue',
    'plugin:prettier/recommended',
    'plugin:nuxt/recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:nuxt/recommended',
    'pretteir/@typescript-eslinnt'
  ],
  plugins: [
    'prettier',
    'vue',
    '@typescript-eslint'
  ],
  // add your custom rules here
  rules: {},
}
