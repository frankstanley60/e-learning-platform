// mathEquationPlugin.js

import Plugin from '@ckeditor/ckeditor5-core/src/plugin';

export default class MathEquationPlugin extends Plugin {
    static get pluginName() {
        return 'MathEquationPlugin';
    }

    init() {
        console.log('The Math Equation plugin is initialized.');

        // Add your plugin initialization logic here
        // This could include adding UI elements, commands, etc.
    }
}
