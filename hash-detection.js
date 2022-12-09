const fs = require('fs');

function detectHash(hash) {
  // Read the JSON file containing the regular expressions and hash algorithms
  const regexHashMap = JSON.parse(fs.readFileSync('regex-hash-map.json'));

  // Create a list to hold the possible hash algorithms
  const possibleHashes = [];

  // Loop through the regular expressions and check if the hash matches
  for (const [regex, algorithm] of Object.entries(regexHashMap)) {
    if (new RegExp(regex).test(hash)) {
      possibleHashes.push(algorithm);
    }
  }

  // If none of the regular expressions match, return "unknown"
  return possibleHashes;
}