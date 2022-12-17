const fs = require('fs');

function detectHash(hash) {
  // Read the JSON file containing the regular expressions and hash algorithms
  const file_data = fs.readFileSync(__dirname + '/regex-hash-map.json')
  const regexHashMap = JSON.parse(file_data);

  // Create a list to hold the possible hash algorithms
  const possibleHashes = [];

  // Loop through the regular expressions and check if the hash matches
  for (const [algorithm, regex] of Object.entries(regexHashMap)) {
    if (new RegExp(regex).test(hash)) {
      possibleHashes.push(algorithm);
    }
  }


  // If none of the regular expressions match, return "unknown"
  return possibleHashes;
}



exports.detectHash = detectHash;
