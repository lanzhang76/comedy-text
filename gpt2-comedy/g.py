import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

#print(gpt2.generate(sess))

text = gpt2.generate(sess,
              length=200,
              temperature=0.7,
              prefix="love",
              nsamples=1,
              batch_size=1,
              include_prefix = True
              )
file = open("read.txt",'w')
file.write(text)
file.close()
print(text)


# curl -X POST -u "apikey:{8xHUge3BkqQtW4wxCa1a9Jn9Q9ra5cgMgfD7bKKdUHNm}" \
# --header "Content-Type: application/json" \
# --header "Accept: audio/wav" \
# --data "{\"text\":\"hello world\"}" \
# --output hello_world.wav \
# "{https://gateway-wdc.watsonplatform.net/text-to-speech/api}/v1/synthesize"