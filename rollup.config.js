import stylus from 'rollup-plugin-stylus-compiler';
import css from 'rollup-plugin-css-porter';
import resolve from 'rollup-plugin-node-resolve';
import commonjs from 'rollup-plugin-commonjs';
import livereload from 'rollup-plugin-livereload';
import { terser } from 'rollup-plugin-terser';

const production = !process.env.ROLLUP_WATCH;

export default {
	input: 'resources/static/index.js',
	output: {
		sourcemap: true,
		format: 'iife',
		name: 'app',
		file: 'resources/static/bundle.js'
	},
	plugins: [
    stylus(),
    css({
      raw: false,
      'minified': 'resources/static/bundle.css'
    }),
		// If you have external dependencies installed from
		// npm, you'll most likely need these plugins. In
		// some cases you'll need additional configuration 
		// consult the documentation for details:
		// https://github.com/rollup/rollup-plugin-commonjs
		resolve(),
		commonjs(),

		// Watch the `public` directory and refresh the
		// browser on changes when not in production
		!production && livereload('public'),

		// If we're building for production (npm run build
		// instead of npm run dev), minify
		production && terser()
	],
	watch: {
		clearScreen: false
	}
};
