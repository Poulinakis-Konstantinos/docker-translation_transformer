# docker-translation_transformer

This is a simple application of using the transformers library for English to German
translation task. The application is then packaged in a docker container.

For more details you can check the accompanying blog post. 

The repo was built for educational purposes. Translation is not very accurate and 
an error related to printing non-ascii character may cause fatal error. 
If you manage to solve it please let me know ;D .

## Instructions
1. Assuming docker is not installed in your system, install docker.
2. From inside the repo run 'docker build -t translator:1.0 .' to build the image.
3. Run 'docker run -it translator:1.0' to create a docker container in interactive mode. If you don't use -it flag
   you will not be able to interact with the translator.
4. Write sentences in the terminal's input.
5. If you solve the ascii related error let me know.
