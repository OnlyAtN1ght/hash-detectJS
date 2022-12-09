const fs = require('fs');

function detectHash(hash) {
  // Read the JSON file containing the regular expressions and hash algorithms
  const regexHashMap = JSON.parse(fs.readFileSync('regex-hash-map.json'));

  // Loop through the regular expressions and check if the hash matches
  for (const [regex, algorithm] of Object.entries(regexHashMap)) {
    if (new RegExp(regex).test(hash)) {
      return algorithm;
    }
  }

  // If none of the regular expressions match, return "unknown"
  return "unknown";
}