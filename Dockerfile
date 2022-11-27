FROM huggingface/transformers-pytorch-cpu

# Set the working directory to app/
WORKDIR /app
# Add the local folder app
ADD /app .

# download model and instantiate the pretrained model
# during building for a faster application.
RUN python3 download_models.py

ENTRYPOINT  python3 eng_de_translation.py
#equivalent command in exec format
#ENTRYPOINT ['python3', 'eng_de_translation.py'] 