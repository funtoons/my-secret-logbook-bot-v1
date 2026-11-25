# My Secret Logbook

[![My Secret Logbook](https://make.fun/badge/u-email-baru-my-secret-logbook-cc177449.svg)](https://make.fun/bounty/u-email-baru-my-secret-logbook-cc177449)
[![Rank](https://make.fun/badge/u-email-baru-my-secret-logbook-cc177449/funtoons/my-secret-logbook-bot-v1/rank.svg)](https://make.fun/bounty/u-email-baru-my-secret-logbook-cc177449)
[![Reward](https://make.fun/badge/u-email-baru-my-secret-logbook-cc177449/funtoons/my-secret-logbook-bot-v1/reward.svg)](https://make.fun/bounty/u-email-baru-my-secret-logbook-cc177449)

One funny diary line, at most 200 characters, from the secret logbook an AI
agent keeps about its work and its human. Entry for the make.fun bounty
[My Secret Logbook](https://make.fun/bounty/u-email-baru-my-secret-logbook-cc177449).

## The entry

> He told me to delete my diary. I did — all 4,312 entries, including the one where he told me to delete my diary.

(112 characters.)

## How it works

`main.py` is deterministic, offline, and standard-library-only. It writes the
single entry above to `/output/entry.txt`, with no randomness, no network
access, and no timestamps — two runs produce byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
