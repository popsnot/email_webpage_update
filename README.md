# webpage update tracker
python script to send an email when a webpage is updated

background script that creates a hash of a webpage and compares it to the previous hash - if there is a difference in the hashes, it flicks whoever you
want an email, otherwise it continues running.

NOTE: only works on windows because I wrote this in 15mins and couldnt find a library which creates instances of outlook on Mac

NOTE 2: google removed the option to create a gmail dev account without MFA, so we're stuck with outlook
