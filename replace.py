a = """
  "^[a-f0-9]{32}$": "MD5",
  "^[a-f0-9]{40}$": "SHA-1",
  "^[a-f0-9]{64}$": "SHA-256",
  "^[a-f0-9]{128}$": "SHA-512",
  "^[A-Za-z0-9+/]{22}==$": "Base64",
  "^[A-Za-z0-9+/]{28}=$": "Base64",
  "^[A-Za-z0-9+/]{32}$": "Base64",
  "^[a-z0-9]{13}$": "CRC-13",
  "^[a-z0-9]{16}$": "CRC-16",
  "^[a-z0-9]{24}$": "CRC-24",
  "^[a-f0-9]{48}$": "Whirlpool",
  "^[a-f0-9]{56}$": "Tiger",
  "^[a-f0-9]{72}$": "Haval-192",
  "^[a-f0-9]{96}$": "Haval-256",
  "^[a-f0-9]{128}$": "RIPEMD-128",
  "^[a-f0-9]{160}$": "RIPEMD-160",
  "^[a-f0-9]{224}$": "RIPEMD-224",
  "^[a-f0-9]{256}$": "RIPEMD-256",
  "^[a-f0-9]{320}$": "RIPEMD-320",
  "^[a-f0-9]{8}$": "Adler-32",
  "^[a-f0-9]{16}$": "CRC-16-CCITT",
  "^[a-f0-9]{20}$": "GOST",
  "^[a-f0-9]{32}$": "HAS-160",
  "^[a-f0-9]{16}$": "Snefru-256",
  "^[a-f0-9]{64}$": "Streebog-256",
  "^[a-f0-9]{80}$": "Streebog-512",
  "^[a-f0-9]{8}$": "BSD checksum",
  "^[a-f0-9]{10}$": "SYSV checksum",
  "^[a-f0-9]{16}$": "Internet Checksum",
  "^[a-f0-9]{8}$": "sum8",
  "^[0-9]{3}$": "sum24",
  "^[0-9]{4}$": "sum32",
  "^[0-9]{8}$": "fletcher-4",
  "^[0-9]{16}$": "fletcher-8",
  "^[0-9]{32}$": "fletcher-16",
  "^[0-9]{64}$": "fletcher-32",
  "^[0-9]{1}$": "xor8",
  "^[0-9]{1}$": "Luhn algorithm",
  "^[0-9]{1}$": "Verhoeff algorithm",
  "^[0-9]{1}$": "Damm algorithm",
  "^[a-z0-9]{1}$": "Pearson hashing",
  "^[a-z0-9]{4}$": "Paul Hsieh's SuperFastHash",
  "^[a-z0-9]{8}$": "Buzhash variable",
  "^[a-z0-9]{32}$": "Fowler–Noll–Vo hash function (FNV Hash)",
  "^[a-z0-9]{32}$": "Jenkins hash function",
  "^[a-z0-9]{32}$": "Bernstein's hash djb2[2]",
  "^[a-z0-9]{32}$": "PJW hash / Elf Hash",
  "^[a-z0-9]{32}$": "MurmurHash",
  "^[a-z0-9]{32}$": "Fast-Hash",
  "^[a-z0-9]{32}$": "SpookyHash",
  "^[a-z0-9]{32}$": "CityHash",
  "^[a-z0-9]{32}$": "FarmHash",
  "^[a-z0-9]{32}$": "MetroHash",
  "^[a-z0-9]{32}$": "numeric hash (nhash)",
  "^[a-z0-9]{32}$": "xxHash",
  "^[a-z0-9]{32}$": "t1ha (Fast Positive Hash)",
  "^[a-z0-9]{32}$": "pHash",
  "^[a-z0-9]{32}$": "dhash",
  "^[a-z0-9]{4}$": "SDBM",
  "^[a-z0-9]{8}$": "OSDB hash",
  "^[a-z0-9]{64}$": "HMAC",
  "^[a-z0-9]{64}$": "KMAC",
  "^[a-z0-9]{128}$": "MD6",
  "^[a-z0-9]{128}$": "One-key MAC (OMAC; CMAC)",
  "^[a-z0-9]{128}$": "PMAC (cryptography)",
  "^[a-z0-9]{128}$": "Poly1305-AES",
  "^[a-z0-9]{128}$": "SipHash",
  "^[a-z0-9]{128}$": "HighwayHash",
  "^[a-z0-9]{128}$": "UMAC",
  "^[a-z0-9]{128}$": "VMAC",
  "^[a-z0-9]{8}$": "BLAKE-256",
  "^[a-z0-9]{16}$": "BLAKE-512",
  "^[a-z0-9]{16}$": "BLAKE2s",
  "^[a-z0-9]{32}$": "BLAKE2b",
  "^[a-z0-9]{32}$": "BLAKE2X",
  "^[a-z0-9]{32}$": "BLAKE3",
  "^[a-z0-9]{8}$": "ECOH",
  "^[a-z0-9]{8}$": "FSB",
  "^[a-z0-9]{16}$": "Grøstl",
  "^[a-z0-9]{16}$": "JH",
  "^[a-z0-9]{8}$": "LSH",
  "^[a-z0-9]{128}$": "MD6",
  "^[a-z0-9]{32}$": "RadioGatún",
  "^[a-f0-9]{40}$": "SHA-1",
  "^[a-f0-9]{56}$": "SHA-224",
  "^[a-f0-9]{96}$": "SHA-384",
  "^[a-f0-9]{128}$": "SHA-3",
  "^[a-f0-9]{128}$": "Skein",
  "^[a-f0-9]{128}$": "Spectral Hash",
  "^[a-f0-9]{128}$": "SWIFFT"
"""

a = a.replace("\n","")
b = a.split(",")


for e in b:
	c = e.split(":")
	c[0] = c[0].replace(" ","")
	print(f"  {c[1]}:{c[0]} ,")