const fs = require('fs');
const assert = require('assert');

const { detectHash } = require('./hash-detection.js');

const validHashes = [
{ hash: '5f4dcc3b5aa765d61d8327deb882cf99', algorithm: 'MD5' },
{ hash: '900150983cd24fb0d6963f7d28e17f72', algorithm: 'MD5' },
{ hash: 'e4d909c290d0fb1ca068ffaddf22cbd0', algorithm: 'MD5' },
{ hash: 'a94a8fe5ccb19ba61c4c0873d391e987982fbbd3', algorithm: 'SHA-1' },
{ hash: 'da39a3ee5e6b4b0d3255bfef95601890afd80709', algorithm: 'SHA-1' },
{ hash: '2f711b9cf1db86b9cfb05fa266fdd5e5c543a72d', algorithm: 'SHA-1' },
{ hash: '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', algorithm: 'SHA-256' },
{ hash: '8e959b75dae313da8cf4f72814fc143f8f7779c6eb9f7fa17299aeadb6889018501d289e4900f7e4331b99dec4b5433ac7d329eeb6dd26545e96e55b874be909', algorithm: 'SHA-256' },
{ hash: '6ca13d52ca70c883e0f0bb101e425a89e8624de51db2d2392593af6a84118090bbaadf6c2b2d19d0e6433f7cb38c2f6e5bc98b8f51e4906f5c5f5d5ba5c5696f', algorithm: 'SHA-256' },
{ hash: '7d793037a0760186574b0282f2f435e737d1f2a3d194c3befe0f3f7e3d74aa3e', algorithm: 'RIPEMD-160' },
{ hash: '8eb208f7e05d987a9b044a8e98c6b087f15a0bfc', algorithm: 'RIPEMD-160' },
{ hash: 'f71c27109c692c1b56bbdceb5b9d2865b3708dbc', algorithm: 'RIPEMD-160' },
{ hash: '9e107d9d372bb6826bd81d3542a419d6', algorithm: 'MD2' },
{ hash: '9e107d9d372bb6826bd81d3542a419d6', algorithm: 'MD2' },
{ hash: '9e107d9d372bb6826bd81d3542a419d6', algorithm: 'MD2' },
];

for (const { hash, algorithm } of validHashes) {
  res = detectHash(hash)
  console.log(res,hash,algorithm)
  assert(res.includes(algorithm));
}