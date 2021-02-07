# Cryptography
PR Link: https://github.com/gracerosemary/casear_cipher/pull/1

**Author**: Grace Choi  
**Version**: 1.0.0   

## Overview
Devise a method to encrypt a message that can then be decrypted when supplied with the corresponding key. You'll also need to devise a way to decipher the encrypted message event when you do not have the key.  

## Getting Started
Create new directory and set up repository on Github

## Architecture
Poetry, Natural Language Toolkit (nltk)

## API
`encrypt`: takes in a plain text phrase and a numeric shift. The phrase will then be shifted that many letters.  
`decrypt`: takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.  
`word_check`: uses `nltk` to check if the decoded word is found in the Enlish language. Returns TRUE if at least 80% words are found.  
`crack`: decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.  

## Change Log
02-06-2021 10:30pm - Finished Lab  