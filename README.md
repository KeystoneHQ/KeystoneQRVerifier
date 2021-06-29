# KeystoneQRVerifier

This repo is based on the work of @fnord123, as the Keystone hardware wallet is simply relaunched from the Cobo Vault branding so both the code base and infrastructure are almost the same. so this tool can be used for verifing Keystone QR Codes.

This repo decodes the Keystone's QR code content in an easily understandable fashion and shows to the user exactly what the Vault is sending to the app, allowing the user to verify that no secrets are being transmitted.

Keystone currently using the BC-UR for QR Codes. Check out the link here: https://github.com/BlockchainCommons/Research/blob/master/papers/bcr-2020-005-ur.md


To run this the following pre-requisites must be fulfilled:
1) Google Protobuf compiler.  
    - On Ubuntu this can be installed by doing:<br>
`sudo apt install protobuf-compiler`
   - On macOS this can be installed by doing:<br>
` brew install protobuf`
   
2) Google Python API client for protobufs. Assuming python3, this can be installed by doing:<br>
`pip3 install --upgrade google-api-python-client`
3) Run (and install if necessary) `make` to build the python modules needed for Google proto3 support.

Once the above pre-requisites are met, the following sequence can be used to verify the safety of the contents of the QR Codes the Keystone shows to the Keystone App during pairing.  If one wants to ensure the security of their cryptocurrency, do **not** load any currency onto the Keystone until the following sequence has been successfully completed.
1) Turn on the Keystone, click on the menu hamburger in the top-left ocrner, and select *Watch-only Wallet*

2) Click on *Keystone App*.  If it is already selected and the *Confirm* button is greyed out, you will need to choose another entry (e.g. *Polkadot.js*), then confirm, then click the *<* arrow to go back and re-select *Keystone App*, then click the (now blue) *Confirm* button.

3) Select any cryptocurrencies desired, then click the check mark at the top-right corner of the screen.

4) On the next screen, click the *Display QR Code* blue button at the bottom.

5) The Keystone will begin rapidly displaying a set of QR codes. Press the *Difficulty scanning? Tap the QR code to adjust.* button.

6) Press the pause button on the resulting screen and use the slider to maximize the size of the QR code, then scan the first image with the Keystone app and with a QR Code Scanner of your choice.  I used 'Codex - QR Code for Windows 10' as a free app from the Microsoft store to do this, but any app can be used that allows saving the resultant text to a file.

7) Scan the first QR code with the Keystone App, it will tell you something like "1 of 3 done". Go ahead and click the right arrow on the vault to display the next QR code, then repeat the process from step 6.  Do this until the Keystone App says it is done, scanning each QR code with both the Keystone App and with your own selected QR code scanner.  

8) Put down the Keystone device and leave the QR code subscreen.  At this point one should never have to display these QR codes again unless pairing has to be done again e.g. with a new phone.

9) Save the text of the Keystone QRcodes (captured using your QR code scanner) into a file accessible by the code in this repository.  The resulting file should look like the [example file in this repo](sample_qr_codes.txt).
*Notes: Since the BC-UR Uses fountain code, it make a bit hard to collect all the qrcodes. so please collect all the qrcodes (m - m) and put into the file. making a video and get the qrcode one by one will be more helpful.*

10) Run the verifier code against the file, e.g.<br>`./keystoneQRVerify.py --file sample_qr_codes.txt`

11) The verifier will decode the QRCode text files and show exactly what they contain. It should look something like this:<br>
```
*************************************************************
Following is entire message sent via QRCode from Keystone to app
*************************************************************
version: 1
description: "keystone qrcode"
data {
  type: TYPE_SYNC
  uuid: "5271C071"
  sync {
    coins {
      coinCode: "BTC"
      active: true
      accounts {
        hdPath: "M/49\'/0\'/0\'"
        xPub: "xpub6D3i46Y43SFfjEBYheBK3btYMRm9Cfb8Tt4M5Bv16tArNBw5ATNyJWjdcMyLxoCdHWTvm3ak7j2BWacq5Lw478aYUeARoYm4dvaQgJBAGsb"
        addressLength: 1
      }
    }
    coins {
      coinCode: "ETH"
      active: true
      accounts {
        hdPath: "M/44\'/60\'/0\'"
        xPub: "xpub6CNhtuXAHDs84AhZj5ALZB6ii4sP5LnDXaKDSjiy6kcBbiysq89cDrLG29poKvZtX9z4FchZKTjTyiPuDeiFMUd1H4g5zViQxt4tpkronJr"
        addressLength: 5
      }
    }
    coins {
      coinCode: "BCH"
      active: true
      accounts {
        hdPath: "M/44\'/145\'/0\'"
        xPub: "xpub6CjD9XYc1hEKcAMsSasAA87Mw8bSUr6WQKrJ1ErLofJPP9sxeZ3sh1dH2S5ywQTRNrXsfXzT686jJNdX2m9KhvMDh4eQM9AdSkkQLLMbDG6"
        addressLength: 1
      }
    }
    coins {
      coinCode: "DASH"
      active: true
      accounts {
        hdPath: "M/44\'/5\'/0\'"
        xPub: "xpub6DTnbXgbPo6mrRhgim9sg7Jp571onenuioxgfSDJEREH7wudyDQMDSoTdLQiYq3tbvZVkzcPe7nMgL7mbSixQQcShekfhKt3Wdx6dE8MHCk"
        addressLength: 1
      }
    }
  }
}
coldVersion: 10001
deviceType: "keystone Essential"
*************************************************************
At this point one should verify each of the XPUBs shown above, and
the UUID shown below (also at the top of the above output). See the
README.md for how to do that.
UUID is 5271C071
```

The UUID used for the identifier of the wallet, which is the master fingerprint of the seed.