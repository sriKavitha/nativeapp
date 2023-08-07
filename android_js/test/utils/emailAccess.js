const imaps = require('imap-simple');

class AccessEmail {

   config = {
    imap: {
        user: 'qa@rosedigital.co',
        // password: '2-fTBy4P9v49',
        password: 'cgkjhwkxxhxgnkcp',
        host: 'imap.gmail.com',
        // user: 'rosedigitalqa@yahoo.com',
        // password: 'Test12345678!',
        // host: 'imap.mail.yahoo.com',
        port: 993,
        tls: true,
        authTimeout: 10000,
        strictSSL: true,
        tlsOptions: {
          rejectUnauthorized: false
      }
    }
    
};

// Retrieve emails with subject: NYL SSO Password Reset Request
  async retrieveEmail() {
    try {
        console.log("Connecting to the QA eMail server... Please wait...\n\n")
        const connection = await imaps.connect(this.config);
        console.log("Hai there!!! Successfully connected to the QA eMail server...\n\n");
        await connection.openBox('INBOX');

        const searchCriteria = ['UNSEEN', ['SUBJECT', 'NYL SSO Password Reset Request']];

        // const searchCriteria = ['UNSEEN'];
        const fetchOptions = 
        {
          bodies: ['HEADER', 'TEXT'],
          markSeen: false,
          struct: true
        }
    
        const messages = await connection.search(searchCriteria, fetchOptions);
        const latestMessage = messages.pop();

        if (latestMessage) {
            const header = latestMessage.parts.find(part => part.which === 'HEADER');
            const emailSubject = header.body.subject[0];
            console.log('Subject:', emailSubject);

            const text = latestMessage.parts.find(part => part.which === 'TEXT');
            const emailText = text.body;
            // console.log('Text:', emailText);

            const urlRegex = /(https:\/\/[^\s]+)/;
            const match = emailText.match(urlRegex);
            let extractedURL = null;
            if (match && match.length > 0) {
              extractedURL = match[0];
            }

            const extractedUrl = extractedURL.trim().substring(0, extractedURL.length - 7);
            console.log("Reset password URL...\n\n",extractedUrl); 
            return extractedURL
        } else {
                console.log('No matching email found.');
               }

      // for (const message of messages) {
      //   const header = message.parts.find(part => part.which === 'HEADER');
      //   const emailSubject = header.body.subject[0];
      //   console.log('Subject:', emailSubject);

      //   const text = message.parts.find(part => part.which === 'TEXT');
      //   const emailText = text.body;
      //   console.log('Text:', emailText);
      // }

      connection.end();
    } catch (error) {
      console.error('Error occurred:', error);
    }
  
  }

}

module.exports = new AccessEmail();
