<h3>Document under construction</h3>
<h2>Documentation for audio transcription using Wav2Vec 2.0</h2>

This project aims at taking raw audio files (both in English and German) to transcribe them so that 
further analysis is possible. 

<h3>Data:</h3>
<h4>Raw data description:</h4>
<ul>
<li>Sampling rate: 44100</li>
<li>Duration: </li>
</ul>
 
<h3>Data Visualization:</h3>
(-visualize length of audio files (before preprocessing and after preprocessing)
-Visualize language
-visualize number of words (content words/ function words))

<h3>Data preprocessing:</h3>
<ul>
<li><strong>Trimming audio:</strong>Participants were allowed to talk for about 5 minutes. Since most of them spoke for shorter than this, the audio 
files were trimmed such that only the portion with audio signal was kept.</li>
<li><strong>Sampling Rate:</strong>Wav2Vect was trained on speech input sampled
at 16Khz, hence the audio files fed to this already-trained model were sampled at the same rate</li>
</ul>

<h3>Model: Wav2Vec</h3>
Since we do not have enough data or resources to build and train our own model, 
I opted to use <a href="https://ai.facebook.com/blog/wav2vec-20-learning-the-structure-of-speech-from-raw-audio/">Wav2Vec</a>,
an already trained model released by Facebook AI. This release consists of a base model one can tune according to the language one wants to transcribe from. For the purpose of this project, I chose two models that had been already trained/tuned 
using both German and English audio files. 

<h4>German Model:</h4> 
<p><a href="https://huggingface.co/marcel/wav2vec2-large-xlsr-53-german">Wav2Vec2-Large-XLSR-53-German</a>: 
Fine-tuned on German data using the <a href="https://huggingface.co/datasets/common_voice">Common Voice</a> dataset.</p>

<h4>English Model:</h4>
<p><a href="https://huggingface.co/facebook/wav2vec2-large-robust-ft-libri-960h">wav2vec2-large-robust-ft-libri-960h</a>:
This model is a fine-tuned version of the <a href="https://huggingface.co/facebook/wav2vec2-large-robust">wav2vec-large-robust</a> model.</p>



