const { execSync } = require('child_process');

// Define the spec files and their corresponding wdio.conf.js files
const specs = [
  {
    spec: './android_js/test/specs/android/MRMNYL-186_sendEmail.spec.js',
    // configFile: './android_js/config/wdio.android.conf.js'
    configFile: './wdio.android.conf.js'
  },
  {
    spec: './android_js/test/specs/android/MRMNYL-186_changePassword.spec.js',
    // configFile: './android_js/config/wdio.changepwd.conf.js'
    configFile: './wdio.changepwd.conf.js'
  },
  {
    spec: './android_js/test/specs/android/MRMNYL-193.spec.js',
   // configFile: './android_js/config/wdio.android.conf.js'
    configFile: './wdio.android.conf.js'
  }
];

// Function to run a spec file with the specified config file
function runSpec(spec, configFile) {
  execSync(`npx wdio ${configFile} --spec ${spec}`, { stdio: 'inherit' });
}

// Execute the spec files sequentially
async function runPWDChange() {
  for (const { spec, configFile } of specs) {
    console.log(`Running ${spec} with ${configFile}`);
    runSpec(spec, configFile);
  }
}

runPWDChange();
