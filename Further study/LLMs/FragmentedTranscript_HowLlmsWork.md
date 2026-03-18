# How LLMs Work

Welcome to Fragmented, an AI developer podcast that helps vibe coders become software engineers one episode at a time. I'm your host, Kaushik.
And I'm Yuri, the other host of Fragmented, where I'd love to talk about using AI to make you a better developer.
So Yuri, if you're in social settings as a developer or a software engineer, inevitably the conversation is going to steer towards AI these days.
The first awkward question that usually comes up is, hey, how do these LLMs work?
Every time someone asks me that question, that Albert Einstein quote keeps flashing in my mind.
If you can't explain it to a six-year-old, you probably don't understand it yourself.
The goal for this episode is to help developers and listeners reduce the awkwardness a little by explaining how an LLM works.
Doing God's work here. Save developers from social awkwardness.
But jokes aside, the advantage here is if you understand how these LLMs work at a slightly more fundamental level, you develop an intuition for them.
Totally, totally.
You get a much better sense of what actually moves the needle when you hear something, right?
Fatib, makes sense or not.
So it's really useful to know.
We want to basically equip you to have an interesting coffee conversation.
So we'll talk about the big pieces.
But each of those pieces, we can honestly do completely independent episodes and talk about those details, which we will do.
All right, that sounds pretty good.
What would be a good starting point, Dan?
If you step back, the goal is to make a computer speak a human language.
But in order to make computers speak that language, what we need to do is take that language and represent it in a form that a computer understands.
And one thing that computers are really good at is math.
In general, math and numbers are things that they understand really well.
So that's exactly what these large language models are able to accomplish.
They're able to take this human language and convert them to just a bunch of ones and zeros that computers understand really well and can have that conversation with you.
This is the framing that I think will be helpful for people to understand.
There's three large steps.
One is if you take language and sentences, you can break that into a bunch of words. We take these words and store them into tokens.
Tokens is the magic word. This is something that a lot of people keep hearing about in this industry.
We'll go into what that is. You know, they're basically just numbers.
But that numbers then alone don't mean anything. We need to build meaning around those different numbers.
And that's where we'll touch briefly into how vectors and the process of embedding comes in.
So those are the three large steps.
And then at the end, we'll recap how it all comes together, right?
If you have that conversation with ChatGPT, how does it leverage all of the concepts we talk about, do that inference, and then naturally come out with a result? So that's the larger framing.
But maybe we should go right to the first step, Yuri. Can you walk us through, where do we start with all of this?
If you have a bunch of words, what does the large language model do with those words? All right, yeah.
So, yeah, just let's say that you have raw text in your input field, right?
You just typed, how does an LLM work?
The first thing is this tokenization step.
So you have this sentence and you have to break down that sentence in tokens.
So you can think of tokens as basically like the smallest semantic unit.
So the smallest thing that has a meaning, but not only that.
Each piece of text in that sentence would have some meaning, right?
So you can think of that as a letter or a suffix or a prefix, a full word, or a number or a symbol, you know?
So let's say, for example, like in the sentence, how does an LLM work? Each of these words would be a token. This would be done by a tokenizer.
And the interesting thing there is, you know, that's the easy way to think about it. But in reality, it's not just a word that translates into a token.
It could be characters, it could be a space, it could be a bunch of special characters.
But to your point, the larger way to think about it is like, in some way, it's broken down into the smallest unit. And that's an atom of an LLM. Exactly.
It's really cool to use a visualizer to see that. So there are some tools.
So you can literally just type in a sentence and you get a sense of what a token is like in that context.
It's really a nice tool to use.
So this whole thing is done by this thing that is called tokenizer.
So that's basically two parts.
There's an algorithm that would split the text, right?
So you have the sentence.
This algorithm would define what is a token in that context.
And then there's the other part, which is basically a hash map lookup. So for each token, there's an ID.
So just say, for example, like the word works in that sentence, how does an LLM works?
So the word works would have a specific ID assigned to it. So the process is basically turning text input into these IDs.
That makes sense.
And to build on that, this lookup table that you're talking about is almost like the dictionary. That's exactly it. Right.
So you literally take any language, take all the possible words, and you make a lookup table for those so that I take words from the sentence, I go to my lookup table, how do I split this thing into tokens?
The process you talk about, like, you know, tokenizer, it's able to use that and then out comes from the other end a bunch of tokens, which are basically just integer IDs. Exactly. That's how they call it. It's a vocabulary.
So the LLM would have specific, each model would have a vocabulary. So that's the process.
So from the input text, you get these integer IDs.
But here's the thing, Yuri, like those integer IDs alone is not enough, right? You know, that token alone is not enough to bring all of this together.
Let me give an example to help illustrate that.
If I say two words, you know, I have apple and orange, both are fruits.
And, you know, if I go to this lookup table that you talked about, maybe we get, you know, for apple, we get the number 10. For orange, we get the number 50.
A single integer ID is too simple. Maybe I can say, hey, the number 50 is closer to the number 10. So they are fruits.
And, you know, if I have some other word that is represented by an integer or a token ID 5000, I know that that is not related to an apple and orange, right? So maybe you have a different word altogether. I don't know. House.
The number house is a completely different integer ID representation, which is 5000, I can at least tell, okay, hey, 10, 50, 5,000. It sounds like the two words 10 and 50 are related to each other.
But that's not the full picture because there's so many dimensions to fruits in themselves, right?
I work at a grocery company, so I can tell you that there's so many things that go around with fruits.
How sour is that fruit? You know, what color is that fruit? 10 and 50 alone does not bridge that relationship, right?
An integer is too simple a construct to talk about all that variety and all of those dimensions.
So how does NLLM handle that problem?
Because so far I'm with you.
I got a bunch of words, convert them to tokens using this table. Great. It's too simple. I need a much more complex relationship to be set up.
How does an LLM do that? Yeah, totally.
Like you said, an integer doesn't have enough value in itself to represent all the characteristics. So the next thing is the embeddings. So from tokens, you go to embeddings.
So embeddings is a weird word, right?
It doesn't make a lot of sense in its own, like in this context, maybe. So to set that up, I think it's good to start with a small analogy.
If you're a developer or designer, you probably know how images are stored.
So images are generally like a matrix of pixel values, right?
So each pixel has a number representing the colors. So let's go with the RGB, so red, green, and blue.
So if you change those numbers, you change the color.
So just imagine a pixel.
It's like a vector or an array, right?
With three values.
So one value for each color, right?
So for that color intensity.
So if you have like, I don't know, like 255, 128, and zero, that's kind of like orange.
That's so good because like, you know, most people understand what RGB values are, right?
So like black, for example, we know is 000.
Exactly, yeah.
And white is what? 255, 255, 255.
So you're right.
Already it's able to represent more depth in terms of describing the color, right?
Because each of those values is a red or a green or a blue value.
So if you want to understand, is this color that you're picking more closer to one of these three values?
Like, is it a more greenish color?
Then I would expect that center value to be higher or something.
I don't know.
Yeah.
Is that the right way to think about this?
That's exactly the direction.
Because if you think about it, it's like each value there would be like the intensity of that construct, of that meaning.
In this case, the meaning is like each color.
So in the context of LLMs, so LLMs are language models, right?
So what we're trying to model here, what we're trying to do here is like to map words and words, the things that they have the most, like the thing that they try to embed in them, like to have in them, like it's meaning.
So the idea is that now every token will need to be converted into like an array, just like a pixel.
But just instead of like having three values, which represent like these intensities of colors, now we get hundreds or thousands of values like representing these abstract semantic dimensions, you know, like this concept, these ideas.
So for each word, they would have multiple dimensions.
And it's really mind-blowing when you think about it.
Like, yeah, it's a very interesting concept.
And this is also what we call vectors, basically.
I think vectors is a fancy term, but yeah, for us software engineers, it's literally just an array of integers.
That becomes a...
It's literally an array, right?
So what you're saying is, just like we took RGB as a vector to represent a color based on the intensity of red, green, and blue, you can do that for words in general.
Taking my example of like an apple and an orange, I can take apple and orange and then all those dimensions I added about color, sweetness, which season it grows in, or you can keep adding those dimensions or those traits as subsequent integers in that vector.
And you can basically just build a much more complex description of that word.
That's exactly it, yeah.
So you go from these basic integer IDs to these vectors that actually represent more meaning.
So there's a paper called Word to VAC that I think maybe was one of the big ones that brought about this idea, this representation.
And I remember in this example, like just imagine that you have this world where the representations you have of meaning, of words are basically just gender, age, and royalty.
You have like these three dimensions.
Now that you have these words, you know, like in this very small example, you would assign a value of these three dimensions, right?
So gender, age, and royalty.
So you think like a boy would have royalty basically zero, but it would have like age, low and gender.
You know, there would be some gradient going from one number to another.
There would be basically like one side you have men and the other side have women.
So boy would probably be closer to men, right?
You stack that up and basically you have these arrays, these vectors, right, that can represent these dimensions for each of these words.
And when you plot that on a graph, like a 3D graph with these words, you would see that the word king and queen, they cluster together on this royalty area, you know, and the boy and girl would be clustering in this age area.
You know, you could literally have like a distance.
You could calculate the distance between words.
So you can, now you can do math with words.
And it's pretty fun because there's the final example, which is like you have the word king and you subtract man and you add woman and you get the same value that you would get for the word queen.
So literally you can do math with words and meaning.
So that's like kind of mind-blowing.
Oh, that is mind-blowing.
Because if you have this 3D space and then you plot these different points, you can literally see related words closer to each other.
Yeah.
Starting right from the beginning of the episode, if you think about the goal of what an LLM does, effectively in the end, you want it to be able to do math on words.
And I think this is that connector piece.
This is where that aha moment comes in if people didn't realize, right?
Which is we've taken all of these words, represented them as vectors.
And if you take the vector for king, man, and woman, like you said, and you do the math, you will land up with a value because you've done the math on them.
And if you look at that value and go to this lookup table to see what the value is for queen, you will find that it's actually the same or similar value. That's how the math is done to build that meaning.
It's so cool because you've arrived at language by doing math on the sequence of words.
Yeah, and that's very powerful because I think the whole point is trying to map this area, like language, into a model to make predictions.
So that's what we're trying to do.
So this covers like how vectors can become meaning.
So the only part now is like, where are the numbers coming from, right?
Who is defining those numbers?
Like you're not gonna manually assign values to that.
It's not gonna work, right?
And also like each word in this example had just three dimensions, but in reality, they have hundreds, maybe thousands of dimensions.
So where and how does the model learn that the king and queen should be closer together in the first place?
Yeah, that's a great question.
In the AI world, you will hear this term thrown a lot called pre-training.
And this is the process of the model learning how to build that map.
Nobody is actually sitting down there and typing in the coordinates.
Nobody tells the computer, hey, an Apple is 70% sweet and 10% crunchy.
So this is the numeric value that must go into the vector representation of that token. That would just take forever. We would never finish if we did that process manually.
So instead, what happens is the model learns the map.
During that pre-training phase, the LLM reads billions and billions of sentences, and it almost plays a guessing game.
It's a game of like, hey, guess the hidden word. Let's take an example that might make it a little more straightforward.
So it sees this sentence. If you have a sentence that says, this is a red fruit that is sweet and crunchy.
When the model is initially created, or if you can use a terminology, when the model is born the very first time, it builds a random map. It has a completely random map.
And in that map, it might think, hey, Apple and some other completely random word like truck are neighbors.
Because when it comes up with this random map, it's just taking all the words from your vocabulary and placing them on a map.
And then it's evaluating it.
In this random map, Apple and truck are neighbors.
Does that work?
Now, when you go back to that sentence, which is like, hey, this is a red fruit that is sweet and crunchy. It does that evaluation phase.
Every time it guesses something wrong, it gets like a sort of nudge, like a mathematical nudge.
It waits and sees, whenever I see the word crunchy or fruit, I'm noticing that the word apple is also somewhere nearby. Probably move this apple vector closer to the fruit vector.
If you think of that as one of these nudges to pull related vectors closer to each other, this machine learning process, when it runs this across billions and billions of sentences, all of these are just tiny nudges. So to billions of these tiny nudges, the model basically is self-organizing itself.
If you think about the spatial matrix of reasoning, it's building this meaning room where all related concepts, you'll start to see related words in this room start to collect or huddle together in the same space.
In some ways, it's so beautiful, but in some ways, it's so dumb.
Through the power of compute, you know, all these fancy NVIDIA GPU processors, that's what they're using them for, right?
Like in the pre-training process, how do we build this spatial map and pull all these related vectors closer to each other so that in the future when someone comes and asks these models questions, they're able to spatially find their way to related words. That's so interesting when you say that.
It's like you're literally creating a space that you can navigate.
It's not just these numbers.
It's actually like there is a space in this large dimension, like this very large dimension of space, right?
This representation of meaning.
It's fascinating, actually.
But I think there's one last piece, and maybe we can close with that piece, inference.
Another one of these terms that you'll hear everyone throw around.
And I know we can't go into full details because that's going to be another 20 minutes.
Based on what people give us feedback, if they want to hear more, we are happy to do that. But pull all of these concepts together for me. Yeah, let's tie it up.
So inference is the last piece.
That's actually what we want to do in the end.
So you start with making a question, right?
You just ask a question to the LLM.
So words become tokens, tokens become embeddings.
And now we have like, oh, you mentioned you have this defined space in this semantic, whatever, that you can navigate and find the next token, the next word.
That's what we're trying to do because that's literally how it works under the hood.
I just need to caveat that this is what a very raw basic LLM does.
And when you actually use Gemini or ChatGPT, they have a lot more on top of this, but they still have this like in the very bottom part.
If you were starting three years back, this is how you would build it basically, right?
Yeah, exactly.
Yeah.
So this is maybe chat GPT too.
But so, yeah, so we were trying to get the next token.
So finally you get to run inference, right?
So the first thing is like, what does that mean?
What is inference?
So inference is just a prediction. You're trying to? What is inference? So inference is just a prediction.
You're trying to predict.
You have to remember this is just a model.
And models are meant to predict things.
So you can, like a meteorologist could use a model to predict weather.
Is it going to rain tomorrow?
There could be a model to predict, I don't know, like stock prices.
So LLMs are language models.
In this case, they just want to predict the next word.
Okay, so we got that out of the way.
I now understand the LNM in LLMs.
Right.
So to be able to predict, the model will just try to output like the probability distribution of its entire vocabulary that we were talking about.
So every possible token now will get a score.
So when you have a sentence, like for example, the best thing about AI is its ability to.
If you input that sentence, you're literally going to sort a list of tokens by their probability.
So you'd have like the higher probability words in the top and then you just sample from those.
And in some models or in most models, they would call this like top K or top P.
This is like a parameter you can pass into the LLM when you're calling it.
So that's exactly, it's like, it's the top candidate picking, the mechanism of picking the top candidate for the next token.
And this is the piece where we are hand-waving the inference because there's a lot of interesting concepts there, right?
Like this temperature.
Exactly, yeah.
Inference in itself is such a complex topic.
So we'll definitely do that in a separate episode.
But to your point, the LLM is a model, so it's go