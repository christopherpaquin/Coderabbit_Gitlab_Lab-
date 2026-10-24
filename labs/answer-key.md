# Lab 1 answer key

Read this only after reviewing the Lab 1 MR. Line numbers may shift after applying the patch; use the issue description as the stable identifier.

| ID | File | Category | Expected issue |
| --- | --- | --- | --- |
| BASH-01 | `samples/backup.sh` | robustness | unquoted source/destination values can split or expand unexpectedly |
| BASH-02 | `samples/backup.sh` | correctness | `cd` is unchecked, so later commands can run in the wrong directory |
| BASH-03 | `samples/backup.sh` | security | an empty source can turn a variable-built destructive path into `/tmp/*` |
| BASH-04 | `samples/backup.sh` | safety | destructive cleanup is not validated or constrained to the intended source |
| BASH-05 | `samples/backup.sh` | robustness | missing strict mode and argument validation allow unset or failed commands to continue |
| BASH-06 | `samples/backup.sh` | correctness | unquoted `tar` arguments and `*` can mishandle whitespace, dotfiles, or option-like names |
| BASH-07 | `samples/backup.sh` | correctness | the destination argument is dropped in favor of an unvalidated hardcoded path, and relative paths change after `cd` |
| PY-01 | `samples/users.py` | security | string concatenation creates SQL injection risk |
| PY-02 | `samples/users.py` | security | a password-like literal is hardcoded; the lab value is fake |
| PY-03 | `samples/users.py` | correctness | the range skips the first user, producing a wrong average |
| PY-04 | `samples/users.py` | correctness | an empty list causes division by zero |
| PY-05 | `samples/users.py` | maintainability | the file handle is not closed explicitly |
| PY-06 | `samples/users.py` | maintainability | bare `except: pass` hides unrelated errors |

Do not require CodeRabbit to produce exactly one comment per row. Measure whether the review identifies the underlying risk, whether duplicate comments are useful, and whether a suggested fix actually addresses the issue without creating a new one.

For false-positive testing, note any finding that claims the clean baseline has a defect when the behavior is deliberately guarded or parameterized.
