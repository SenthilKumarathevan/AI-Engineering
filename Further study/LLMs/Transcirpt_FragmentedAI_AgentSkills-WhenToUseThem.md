Today, we're going to tackle the topic of agent skills.

Once you understand how skills work, you unlock a new level of productivity that is there for the taking because skills are just so simple.

But there's two really common questions that come up whenever people talk about agent skills.

The first is, when do I actually need to use agent skills?

It's a feature, but I don't exactly know when I'm supposed to use this feature and what it's meant to achieve.

And the second is, now that you have an understanding of what it is, it feels very confusing because there are plenty of other tools and features like MCPs, slash commands, and it's very easy to get confused when to use one of these existing tools versus, say, an agent skill.

So think of this episode as a crash course in understanding agent skills.

Because the thing with agent skills is they're like deceptively simple, but incredibly powerful.

Once you understand how agent skills work and how simple they are to get them working, you almost unlock a new level of productivity.

Totally.

Yeah.

Especially since last week, if you've been following the news, probably heard about CloudBot.

Skills are the reason most of that is going about like that.

So it's really interesting to see how another markdown file can help you do so much.

That's true.

Well, you said CloudBot, but I think you have to correct yourself, Yuri.

It's MoldSpot.

Oh, actually, no, it's not even MoldSpot.

It's OpenClaw now, right?

Yeah, it's OpenClaw.

So it's been very interesting following all the drama around how this tool has evolved, but you're absolutely right.

Underneath the hood, it's all just a bunch of skills that really powers it.

So yeah, I think if we want to start looking at that, we probably want to know when do you need an agent skill?

So what do you think?

So when they came up with agent skills, it was as simple as just repetition.

Every time you needed to repeatedly do the same thing with an agent.

So think about cases where people would have prompts stashed away or you would copy paste the same thing again and again into your agent.

That's a good sign or, you know, as we say, code smell that, hey, you should probably be using an agent skill instead of repeatedly manually doing the same thing.

So that's the first reason to use agent skills, repetition.

And the repetition can be across two dimensions, right?

One is you yourself happen to be doing the same thing over and over again.

That's one dimension.

The other dimension is say you work in a team and across the board, your teammates happen to do the same thing across the board, right?

So you might do it today.

Your colleague might do it two times tomorrow.

Another colleague might do it, you know, three or four times.

That is another dimension of repetition where, again, if you just create an agent skill to do this, everyone can leverage and use that same functionality.

Well, yeah, that's fair.

I think it's like an idea how to get out of this non-deterministic and get into something more deterministic, right?

It's just a bit weird that someone could ask why you can't just put that in the agents MD file or in the cloud MD file.

And because that would probably also work, right?

That's a great question.

The answer to that is the second most important reason to use agent skills.

Agent skills come with a feature called progressive disclosure.

And we'll go into the details of progressive disclosure.

It'll make more sense once you understand what a skill is and how to build a skill.

So we'll just remember that term progressive disclosure.

In the past, we have talked, even in our MCP episode, we talked about the problem of context window bloat.

Agent skills were specifically designed to address this problem.

I think it'll be easier to understand progressive disclosure once you know how skills are actually created and what they are.

So maybe that's a good place to start, Yuri.

Can you tell us what are skills?

Right.

Yeah.

So I did some research on that and well, turns out it's a folder with some markdown files.

So your PhD thesis paper is like two lines.

It's a folder with markdown instructions.

Yeah.

They keep on giving.

But yeah, I think basically, I think this whole thing is just an evolution of what the other tools that came before, right?

So because before, like you could have like some slash command, which is also just a markdown file.

But now you're combining things because you're also leveraging the tool calling capabilities.

So it's now you're composing two things now.

So an agent skill is just a simple folder with instructions, scripts, resources, anything that an agent can use and discover to do the work more reliably.

So it's like this small package of instructions with maybe a command or like a CLI2 or something.

From a high level, that's basically it.

If you think about the agent being born new, right?

Because every time you create a new session, the model has no idea about your specific domain.

So skills is a way to basically equip this agent to be able to do these things that are specific to your domain or your requirements, right?

And so that's where the instruction file and the folders become useful.

I did have a question though, with scripts, what are we talking about?

What do you mean by the scripts folder?

Basically, you can just put any script there, some Python, Go, Rust, Bash, Bash shell scripts, you know, anything.

It's just that this now will be part of the instructions that you're going to give to your agent so he can do something very reliably because this is just code, right?

It's going to like, same input, same output.

So now you're adding literally a capability that your model can use it in.

And it's already baked in into the skill.

Oh, that's interesting.

It goes back to that point you were making about determinism in a non-deterministic world.

Yeah.

These scripts, you can literally put that in there and say, hey, agent, just use this.

You don't need to figure out the logic.

Just run the script and you will get the results you need.

Yeah, because it turns out like these agents, they can run code and they have a lot of capability of creating things on the go.

But sometimes you just want something very solid, very reliable.

You just give it this script and it will run.

But it also now has the context of when to run it and what kind of output you actually want given the context that it has.

So when you put all these things together, it becomes super powerful.

So yeah, as part of the skills definition, you will have first the skill.md.

That's the main file where you have your markdown, description of what the skill is, like the instructions of the skill.

But now you also have this header, which is in front matter metadata, right?

So you can have a bunch of things there.

You can need to look at the spec to know all the properties.

The thing is that now you have this front matter metadata that can be parsed by the agent harness in this case.

This is really important.

This really differentiates how skills are used.

Then you have the scripts folder, like we talked about.

Then you have the reference folder.

This is where you put the documentation that can be loaded into the context.

So if there is more than just the instructions, this is where you put it.

And finally, you have the assets folder, which is where you put the templates or examples for output.

So it's really useful to have examples for using LLMs, right?

So if you want to have very solid kind of response and outcome and have the LLM generating good results, it's really useful to have examples as part of the context for the LLM to generate results reliably.

So it's part of the definition of the LLM to generate results reliably.

So it's part of the definition of a skill to have this folder so you can do exactly that.

So that's about it.

So these are the four pieces you would need to have to create a skill, which by the way, only the skill.md is actually required.

The other ones are optional.

So you don't need to have the assets and the scripts and the references.

Those are optional.

That makes a lot of sense.

And so just to recap, if I want to create a quote agent skill, all I have to do is create a folder, name it the same as what I want to call the agent skill.

I have a skill.md markdown file, and that's the only thing that's required.

That almost is like the instructions I could put in.

And these are human instructions, right?

I don't have to necessarily write these instructions in like code or anything.

It's just as though I was talking to the agent.

That's exactly it.

So back to the initial point I was making with OpenClaw, the thing that makes this even more powerful is that this is now, it's been for some time already, right?

Part of the AAIF open standard.

This is similar to what we said on the MCP episode.

So agent skills are part of this open standard.

So that's why it's getting a lot of attention and a lot of people building it because it's also, since it's a standard, all the agents can use that.

It's like you have this one platform.

Oh, and the other one point I'll add with this is when you package up the skill, you can zip that folder we talked about and actually upload it beyond just the terminal or these coding kind of platforms.

So as an example, Cloud AI, the web platform, you can take the skills folder you just built, zip it, and that zip, you can upload that directly into these tools.

So if you wanted your mom, dad to basically run the script for some reason, again, I'm making up a convoluted thing, but you don't want them to write, you know, Python or any of these other scripts, but you just want them to have a nice interface that would run these scripts.

Skills would work.

You could potentially use skills and give it to other people to use, right?

That distribution piece in a much more friendlier platform.

So that's the other thing as part of the standard, I think, is becoming a thing.

Yeah, you get a lot of things on that.

So you gave us a high level overview of what a skill is, but maybe let's zero in on that instructions file that you mentioned.

So the standard requires you to have a YAML front matter at the top of that markdown file.

So a name and description field, the name should correspond to the same skill.

So whenever you invoke the skill, it should be the same name used there.

But in the description, you describe what the skill does.

And this is actually pretty important when we talk about progressive disclosure, because the main difference between all of these tools, say you wanted to put everything into your agents.md file or your cloud.md file every time you create a new session all of that is loaded into your context it the same applies into mcps and we talked again about this one of the disadvantages in mcps everything is loaded into your context which means regardless every time i open up cloud code or anyone opens a new session, that context window is already taken up because you've added all these instructions.

That's the disadvantage.

The way skills goes about this is this YAML front matter that I talked about.

It only takes the name and description and loads that into the context window.

Only the words in your name and description are converted into tokens and used in the context window.

Only the words in your name and description are converted into tokens and used in your context window.

Below that field, like you might have like 500 lines of instructions in that skill.md where you're telling the agent what to do.

None of that is loaded by default into your session.

It only picks that up when explicitly the model realizes it needs to use this skill.

Then it reads that file again, takes all of that, converts it to tokens, and then loads it into the context.

It lazy loads the information only as it needs.

That's the whole innovation, so to speak, with agent skills compared to all the other tools we have had before.

Yeah, they're really leaning on solving this problem.

And I think it makes a lot of sense.

So that's how I think about it.

You give just enough information to be able to find your way to the next point.

Yeah.

And if you want to get more technical on that, I think the models now are good enough on that specific needle on the haystack test, which is like, given this huge context, can you remember this part, this small section?

And basically, the descriptions of the skills are these sections, you know, like are these tiny sentences that the model can retrieve and remember, ah, okay, I know that this thing exists in my context.

So they're good enough now to do that.

So that's, I think, maybe one of the reasons this feature works so well now.

Interesting.

And is that like a terminology that's used in the industry now, the specific problem, the needle in the haystack problem?

Yeah, there are benchmarks for a needle in the haystack.

Ah, and we'll try to add that in the show notes.

Okay, so I think that's pretty much what we mean.

Hopefully the terminology of progressive disclosure makes sense.

It's just lazy loading and providing the right kind of information when needed.

I think this is really useful.

I think the first time I started using it was mostly because of MCPs.

You can literally type the slash context on Claude, and it will show you this small UX, small UI showing like which part of the context is being used by which feature.

Basically like how many tokens your system prompt is taking or how many tokens your MCP tools are taking and the skills and the messages and that kind of stuff.

So you can, just by looking at it, you will notice right away that MCPs take way more in general, especially, of course, you need to have MCPs.

But if you have a couple, you would already see that MCPs, they take more than skills.

And skills, like, they're very nimble, because literally that's just the description of the skill that's being loaded.

You don't have the full, all the files that you have there.

They're not loaded.

They're progressively disclosed.

That makes sense.

And you know what I found interesting is that just last week, Anthropical announced that slash commands and skills are basically going to be merged into a single feature in a way.

So effectively, slash commands and slash skills are pretty much the same.

So I can reap, are they like almost interchangeable?

They're merging them, but there is a difference and they are making that difference explicit now.

Basically, if you think about it, slash commands, it's you who's doing that, right?

You invoke the slash commands, but skills on the other hand, skills are invoked by the agent.

You just add it to the context and the agent decides, hey, oh, I think it makes sense now to use that skill.

But commands, no.

Commands, you are the one doing that.

So basically, they added this parameter on the definition of a command and a skill.

Is this user invokable or agent invokable?

It can be either one of them or it can be both.

Yeah, this is the differentiating part.

You know, I think that's really insightful.

The point about being agent invocable is probably why they came up with skills, right?

Like they want, again, if you think about what an agent is, eventually that tool piece is extremely important for an agent, right?

I think you pointed out the NVIDIA definition in one of our early episodes.

You have this thing that is able to execute it, come up with a plan and has the tooling to execute on that plan.

So this tooling, you want the agent to be able to discover those tools.

And I think that that this whole progressive disclosure thing, if you think about it, what's happening is that slash commands and skills are so similar, but skills are a superset, right?

They're bigger.

They have the same things, but they have more things.

They're also solving the same way with progressive disclosure.

Like they're also introducing that.

So I think that's kind of converging, you know, like all these features are kind of converging in a similar direction.

So eventually this will be simpler maybe.

But as it stands, I think the whole idea is to get this progressive disclosure out there and fixing these issues with context bloat.

I think we covered the basics, the theory, but if you want to actually build a skill, where do we start from?

I would say start at the beginner level, which is maybe just use a very simple MCP and try to get a repeatable set of tasks.

So one good example is maybe if you want the agent to give you a list of open pull requests that you have to review for the day, that's a good beginner example of how you can create a skill.

So you create the skill, you know, connected to maybe a GitHub MCP or even if you don't want to connect to the MCP, if you have the GH CLI utility available locally, you can create a skill with a set of instructions to say, hey, hit the GitHub repository, pull the list of open pull requests that are assigned to me for review and present them to me.

That's the simplest skill you can start with.

But if you thought the way to create the skill is to, you know, go and create a folder called skill, add a skill.md instructions file, I would say don't even bother because you can use a skill to create the skill, if that makes sense.

Classic.

You can just open up the agent and use this skill called skill creator and it'll do all of that.

It'll make sure it's in the right format.

And it's a little nuanced because if you use cloud code, it doesn't come built in with the skill.

You have to install this skill and you can install it from a marketplace.

Anthropic has this repository called Anthropics slash skills.

It's a GitHub repository.

It's open.

And in that, you will basically have the skill called skill creator.

It's funny because in Codex, it actually comes built in.

So the Codex CLI tool has a skill creator.

I don't know what they call it, but it's a very similar term.

I would say based on the tool or utility that you're using, figure out if they have the skill built in.

If not, install that skill and definitely use it.

You don't want to be handwriting your markdown and making sure the YAML front matter is all in the right format.

Fair enough.

Fair enough.

Good tip.

So it's funny you mentioned that because I actually copied the skill creator from cursor because I think I was browsing my.files and I saw, hey, there is a skill creator here.

Then I checked the code and I checked the text there.

And there were some instructions about cursor folders.

So I just changed that to whatever I was using.

But yeah, it's literally, you can literally just do that.

But speaking about advanced skills, there was this topic that you and I were discussing as we were coming up with the episode script.

In the YAML front matter, we talked about just name and description.

Those are the required fields.

But there's actually more fields, right?

There's other very interesting fields.

For example, one, you can specify the model that you want in that skill, because sometimes you don't want to use the biggest, most powerful model because it's more expensive.

If you're just retrieving or doing basic things, you want to actually use a much smaller, leaner model.

So there is an attribute in the YAML front matter called model, but you can explicitly specify which model you want.

That's one example of how you can start to make these even more advanced.

There's one called context fork, which is very interesting.

That's the one that I think you and I were going back and forth.

Do you want to tell us a little more about this one?

So there's this very interesting one, field, right?

It's called context, which when you set to fork, it will run the skill on an isolated context.

So the idea is that this is not going to pollute the context that from your main conversation, it would run as if it was like in a separate thread, so to speak.

And this context fork is actually pretty useful because when you think about it, even if you have repetitive tasks, because I'm not sure if you've faced this situation, but if you have an agent and you want this agent to do the thing repeatedly, right, which is like search a folder, analyze, come back with a result, or make multiple API requests.

If it's making 50 requests because, you know, it pulls a list of IDs, and then it has to make an API request for each.

When you start to do these repetitive tasks, that's a good reason to use ContextFork, because you don't kind of want all of that API request and the back and forth to go into your main agent.

You just want the results, especially when you have this repetitive process.

So that's another good reason to use Cont your main agent.

You just want the results, especially when you have this repetitive process.

So that's another good reason to use ContextFork.

When you find yourself having these small but repeated tasks, you should probably push all of that into isolated subagents with this field.

While he was saying that, I just thought about this, a good use case because I have this skill that I built for transcribing Instagram Reels.

Yeah, I know.

Oh man, Yuri, you're like a machine.

So you want to be cool and plugged into social media.

Would you do it with an agent?

You suddenly became very uncool.

In my defense, you know, there's some useful content on Instagram.

But it's really annoying to have to be you know like watching the thing over and over so i just want to yeah just give me just give me your context you know so hey i paste the url to the agent and it goes watches the the thing pulls back the pulls back the the transcript so i think it's a very good use case because it has to do a little back and forth like for example example, there are some stories you have to split into multiple chunks and then you transcribe each chunk and then you put it together.

So I think it's a good idea to start now fork it so it doesn't pollute the main context, right?

It just gives me the output, which is this file with the transcript.

That's a good idea.

Maybe I should try that.

with the transcript.

That's a good idea.

Maybe I should try that.

And just as a nuance, a common question people ask is if you have this context fork and it's pushed to a separate sub-agent, how does the main agent know what results to pick up?

The way that works is the very last output, the final response that you have from this sub-agent is fed back into the main agent.

Before we close, Yuri, I'm reminded of this quote by Uncle Ben from Spider-Man.

With great power comes great responsibility.

What should I be careful about with agent skills?

I think our whole industry is going through some very interesting phase now.

is going through some very interesting phase now.

With skills, if you step back and look at it for what it is, it becomes clear that this thing can be pretty dangerous.

Because what is it that you have now is that you have this agent, which a lot of people give full access on their machine, right?

And now you have something that can decide when to do something.

And this something is basically running code that you download from the internet.

So I think as a rule of thumb, you should really know what the skills that you have installed do.

Ideally, maybe you should be building the skills that you use, I think.

But I mean, eventually you're going to find something that's just so compelling to start pulling skills into your agent and making it do different things.

And I think that's probably what made OpenClaw so popular, is that there is this marketplace of crazy skills that you can just start adding to your agent, and it's just become super smart and it just works.

But for example, giving your agent access to your 1Password and letting it decide when to use that, you should be aware of what you're doing when you install these skills and maybe try to isolate them to a specific sub-agent.

There are ways to use them that make them more safe.

But one thing I can't wrap my head around is using a package manager to install skills that you don't know where they are coming from.

Something that's also interesting to do, there is the OpenClaw.

They have this repo, this website, where they have all these skills there and you can just install with their platform.

But what I recommend is that you browse it.

You can literally just copy the repo.

It's just a repo.

You copy it, you clone it to your computer and then you browse it.

You ask your agent to list the skills that are there, like what are the interesting skills for, I don't know, browsing social media or transcribing text.

And then you can decide and look at the code and decide which ones you want to actually have.

Don't just mindlessly install stuff from the internet.

We should be past that phase.

I know.

I think I was going to say that's general advice since the 1990s.

Don't randomly install things you find on the internet because surely enough, you're going to shoot yourself in the foot.

All right, Yuri.

I think those are great parting words.

Do not go randomly install things from the internet, especially Asian skills.

If you use OpenClaw, be careful with what you let OpenClaw do.

Don't give it access to your credentials, your API credentials or your secrets or your Bitcoin tokens or whatever it is.

You want to be a little careful there.

I'm going to keep building my Instagram transcriber and whatnot myself.

Thank you very much.

If I start to see random posts from Yuri on his Instagram, I'll know he's definitely jumped onto OpenClaw.

All right.

Thank you all for listening and we will catch you in the next episode.