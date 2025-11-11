# What these terms mean (and when to use—or avoid—them)
# Argon2

# What it is: The modern, password-hashing winner of the Password Hashing Competition. The recommended variant is Argon2id (hybrid of Argon2i/Argon2d). It’s memory-hard (tunes RAM usage) and time-hard (tunes CPU), making GPU/ASIC cracking expensive.

# Use when:

# Storing user passwords (best-practice choice today).

# You can control/tune memory and time parameters (e.g., memory_cost, time_cost, parallelism) to fit your hardware.

# Avoid when:

# You need a fast general hash (e.g., file checksums) → use SHA-256/512 instead.

# Dependencies are unavailable (e.g., constrained environments). Then fall back to bcrypt or PBKDF2.

# Salt

# What it is: A random, per-password value mixed into the hash. It’s not secret and prevents precomputed/rainbow-table attacks. With bcrypt/Argon2, the salt is generated and stored inside the hash string—no extra column needed.

# Use when:

# Always, for password hashing (bcrypt/Argon2/PBKDF2 all do this).

# Generating unique salts per password (let the library do it).

# Avoid when:

# Treating salt like a secret key (it isn’t).

# Reusing a single, static “salt” for everyone (defeats the purpose).

# Optional advanced concept: a pepper is a secret, app-wide value (kept in env/secret manager) that you concatenate before hashing. It’s in addition to a salt and not stored in the DB.

# Hashing

# What it is: One-way function mapping input → fixed-size output. Cryptographic hashes (e.g., SHA-256) are collision-resistant and preimage-resistant.

# Use when:

# File integrity (SHA-256 of downloads).

# Message digests in signatures/HMACs.

# Password storage but only via password hashing KDFs (Argon2, bcrypt, PBKDF2)—not raw SHA-256.

# Avoid when:

# You need to decrypt later (hashes are one-way; use encryption for that).

# Storing passwords with a fast hash (e.g., raw SHA-256) → too easy to brute-force.

# bcrypt

# What it is: A battle-tested password hashing algorithm (Blowfish-based) with a tunable “cost” factor (work factor). Salt is built in.

# Use when:

# Password storage in most apps—portable, widely supported, easy to tune (rounds/cost).

# Argon2 isn’t available; bcrypt is still solid.

# Avoid / watch-outs:

# 72-byte input limit: bcrypt ignores characters after 72 bytes. Long passphrases can get truncated. (Mitigation: enforce reasonable max length; or pre-hash with SHA-256 carefully and consistently before bcrypt—be sure you’ll never change that pipeline later.)

# Not for non-password use cases where a fast hash is appropriate.

# The time functions (Python)

# What they are: Tools to measure durations or wait.

# time.time() → seconds since Unix epoch. Fine for timestamps; OK-ish for coarse timing.

# time.perf_counter() → high-resolution timer for benchmarking code.

# time.monotonic() → clock that never goes backward; good for timeouts/retries.

# time.sleep(n) → pause execution.

# Use when:

# Quick performance comparisons → perf_counter().

# Storing “when an account was created/locked” → time.time() (timestamp).

# Avoid when:

# Using time.time() for tiny benchmark measurements (use perf_counter() instead).

# Relying on wall clock for security-sensitive timing (stick to monotonic/perf counters).