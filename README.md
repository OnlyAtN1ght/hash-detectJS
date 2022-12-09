### hash-detectJS

detect-hash is a JavaScript module that allows you to detect the algorithm used to produce a hash. It works by matching the hash against a list of regular expressions and hash algorithms, and returns a list of possible algorithms that the hash could have been produced with. This can be useful for security and forensic applications.


## Installation
To install this module, run the following command:

```
hash-detectjs
```

## Usage

To use this module in your JavaScript code, you can import it using the `require` function:

```
const detectHash = require('detect-hash');
```

```
// Use the detectHash function to detect the algorithm used to produce a hash
const algorithm = detectHash('<hash>');
```

## Examples


Here are some examples of how to use the `detectHash` function:

```
// Import the detectHash function
const detectHash = require('detect-hash');

// Use the detectHash function to detect the algorithm used to produce a hash
const algorithm = detectHash('<hash>');
console.log(algorithm); // Output: [<algorithm1>, <algorithm2>, ...]

// Use the detectHash function with a custom list of regular expressions and hash algorithms
const regexHashMap = {
  "<regex1>": "<algorithm1>",
  "<regex2>": "<algorithm2>",
  ...
};
const algorithm = detectHash('<hash>', regexHashMap);
console.log(algorithm); // Output: [<algorithm1>, <algorithm2>, ...]
```


## Configuration

By default, the `detectHash` function uses a built-in list of regular expressions and hash algorithms to detect the algorithm used to produce a hash. You can customize this behavior by providing a custom list of regular expressions and hash algorithms in the form of a JSON object. For example:

```
const detectHash = require('detect-hash');

// Customize the list of regular expressions and hash algorithms
const regexHashMap = {
"<regex1>": "<algorithm1>",
"<regex2>": "<algorithm2>",
...
};

// Use the detectHash function with the custom list of regular expressions and hash algorithms
const algorithm = detectHash('<hash>', regexHashMap);
```

## List of supported hash

**Cryptographic hash functions** : MD5, SHA-1, SHA-256, SHA-512, Whirlpool, Tiger, Haval-192, Haval-256, Streebog-256, Streebog-512

**Binary-to-text encoding scheme** : Base64

**Checksum algorithms** : CRC-13, CRC-16, CRC-24, CRC-16-CCITT, Adler-32, Internet Checksum, sum8, sum24, sum32, fletcher-4, fletcher-8, fletcher-16, fletcher-32

**Russian cryptographic hash functions:** : GOST, HAS-160, Snefru-256

**Checksum algorithms for BSD and SYSV systems** : BSD checksum, SYSV checksum

**Hash functions for hash tables** : Pearson hashing, Paul Hsieh's SuperFastHash, Buzhash variable, FNV Hash, MurmurHash, Jenkins Hash

**Cryptographic hash functions based on the RACE Integrity Primitives Evaluation Message Digest (RIPEMD) algorithm** : RIPEMD-128, RIPEMD-160, RIPEMD-224, RIPEMD-256, RIPEMD-320: 

## Contributing

We welcome contributions to this project. If you have found a bug or have a feature request, please open a new [issue](https://github.com/OnlyAtN1ght/detect-hash/issues) and provide as much information as possible.

If you would like to contribute code to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and commit them to your branch.
4. Push your branch to your fork on GitHub.
5. Open a new [pull request](https://github.com/OnlyAtN1ght/detect-hash/pulls) and provide a detailed description of your changes.

## Improuvment 

**Add support for more hash algorithms:** The module currently only supports a limited number of hash algorithms, and adding support for more algorithms could make it more useful for a wider range of applications.

**:Optimize the performance of the module:**: The module currently uses a brute-force approach to matching hashes against regular expressions, which may not be efficient for large datasets. Optimizing the performance of the module, such as by using faster algorithms or parallel processing, could make it more practical for use with large datasets.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

