const speech = require('@google-cloud/speech');
const fs = require('fs');

const client = new speech.SpeechClient();

const filePath = 'path/to/audio/file.wav';


const file = fs.readFileSync(filePath);
const audioBytes = file.toString('base64');

const audio = {
  content: audioBytes,
};

const config = {
  encoding: 'LINEAR16',
  sampleRateHertz: 16000,
  languageCode: 'en-US',
};

const request = {
  audio: audio,
  config: config,
};

client.recognize(request)
  .then(response => {
    const transcription = response[0].results
      .map(result => result.alternatives[0].transcript)
      .join('\n');
    console.log('Transcription:', transcription);
  })
  .catch(err => {
    console.error('Error:', err);
  });