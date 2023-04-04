# Secretbox

In this activity, you will practice encryption by using the Secretbox demo from TweetNaCl.js.

## Instructions

1. Open your browser and navigate to the [Secretbox demo](https://tweetnacl.js.org/#/secretbox) from TweetNaCl.js.

2. Once you’ve navigated to the site, you should see four text boxes on the screen. The boxes are labeled Key, Nonce, Message, and Box.

3. Type an arbitrary message into the Message text box on the lower-left side of the screen. This message is a secret!

4. Next, click the Random button that is located to the right of the Key text box. This button will generate a key, or a random alpha-numeric series of characters, in the Key text box.

    Once your secret message is encrypted, you will be able to use this symmetric key just like a password to access the message.

5. Secretbox also requires that you add a nonce to your message. Recall that “nonce” stands for “number used once.”  To generate the nonce, click the Random button that is located to the right of the Nonce text box.

6. Next, click the blue Encrypt button found beneath the Message box. This will encrypt the message.

7. Take note of what the Secretbox tool returns as the encrypted message in the Box text box on the lower-right side of the screen.

8. Now, you have an encoded message and the key&mdash;the “password”&mdash;that will decode it. To decode the message later, copy the encrypted message, the key, and the nonce to a secure place for storage.

9. For now, leave the key, nonce, and encoded message in their respective text boxes. Delete the original message from the Message box.

10. Then, click the green Decrypt button, which is located beneath the Box text box. The original message should reappear in the Message box.

     * Remember to delete the message you encrypted from the `message` box before hitting decrypt so you see the decryption occur.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
