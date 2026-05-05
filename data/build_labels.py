"""Build labels-v2.json for the N=100 study by extending existing labels.json.

Adds 70 new LinkedIn samples pulled via Unipile, each labeled by Claude judgment
with rationale + class + confidence. Output: labels-v2.json with all 100 samples.
"""
import json
from pathlib import Path

HERE = Path("/sessions/compassionate-affectionate-sagan/mnt/Claude-Research/aura-research")
existing = json.loads((HERE / "labels.json").read_text())

NEW_SAMPLES = [
    # ─── clear_ai (template / engagement-bait / vendor-PR) ───
    {"id": 31, "label": "mak_singh_unlock_greatness", "class": "clear_ai", "claude_score": 88, "confidence": "high",
     "rationale": "Pure motivational-template skeleton. ➡️/✔️ bullet stacks, 'Most people don't lack X. They lack Y' rhetorical pattern, 'No fluff. Just results.' closer, framework-naming ('Unlock Your Greatness').",
     "text": "Here's a tighter, more punchy version clean, authority-led, and built for engagement:\nMost people don't lack potential. They lack direction… and execution.\nThat's why I created Unlock Your Greatness. This isn't motivation. This is a framework to move from stuck → to success.\nI've seen it too often:\n➡️ People second-guess themselves\n➡️ Stay where they've outgrown\n➡️ Lose momentum and identity\nNot because they can't… But because they don't have a clear path.\nThis changes that.\n✔️ Clarity of purpose\n✔️ Confidence & resilience\n✔️ Aligned action\n✔️ Real execution\nNo fluff. Just results."},

    {"id": 32, "label": "real_estate_emoji_template", "class": "clear_ai", "claude_score": 90, "confidence": "high",
     "rationale": "🔑/🌟/🚀 emoji template with parallel bullet structure. 'Stop Struggling, Start Succeeding' alliteration, 'Master the Art of X' parallel headers. Textbook engagement-bait skeleton.",
     "text": "🔑 Unlock Your Real Estate Potential: Stop Struggling, Start Succeeding! 🔑\n\nAre you an investor finding it challenging to generate leads? You're not alone, but the good news is, there's a way forward! 🚀\n\nIn the ever-evolving world of real estate, having the right strategies and support can make all the difference. Here's how you can turn the tide and start attracting quality leads:\n\n🌟 Master the Art of Lead Generation: Learn innovative techniques to identify and connect with potential clients who are ready to invest. \n\n🌟 Enhance Your Networking Skills: Build meaningful relationships that open d"},

    {"id": 33, "label": "anchor_bridge_template", "class": "clear_ai", "claude_score": 80, "confidence": "high",
     "rationale": "Hashtag-only post with abstract corporate phrasing. 'Digital transformation dominates industry conversations' is generic AI thought-leadership.",
     "text": "Digital transformation dominates industry conversations but behind the scenes, the challenges are still very real.\n\n#AnchorBridgeConsulting #DigitalTransformation #FutureOfWork #BusinessTransformation #Innovation"},

    {"id": 34, "label": "webanix_corporate", "class": "clear_ai", "claude_score": 85, "confidence": "high",
     "rationale": "Pure corporate B2B template. Jargon stack (automation, real-time insights, scalable solutions), generic 'Is your business ready for the next step?' rhetorical CTA, hashtag flood.",
     "text": "B2B companies are no longer relying only on websites - they're investing in smart applications to improve efficiency, customer experience, and business growth. From automation to real-time insights, apps are becoming the future of digital transformation. Is your business ready for the next step? Let's build scalable solutions together.\n\n#b2b #businessgrowth #digitaltransformation #mobileapps #webapplications #customsoftware #softwaredevelopment #businessautomation #techsolutions"},

    {"id": 35, "label": "salesxchange_hashtag_stack", "class": "clear_ai", "claude_score": 90, "confidence": "high",
     "rationale": "Two sentences plus a 20-tag hashtag stack. Maximum opacity-to-substance ratio.",
     "text": "https://lnkd.in/eVXtqFFB - A transformative B2B strategy focusing on digital selling, eradicating waste, and boosting ROI. Shift from B2C methodologies to those designed for B2B success.\n\n#b2bsales #b2bnewbusiness #digitalselling #b2bsaas #b2bgrowth #B2BSaaS #DigitalTransformation #SalesStrategy #LiveStreaming #SaaSMarketing #BusinessGrowth #TechInnovation #LeadGeneration"},

    {"id": 36, "label": "nigel_link_bait", "class": "clear_ai", "claude_score": 85, "confidence": "high",
     "rationale": "Link + 'must-read for CEOs and investors' framing + hashtag stack. Pure click-bait template.",
     "text": "https://lnkd.in/eyjTZQ7p - Unveil 'The Frightening Reality of B2B SaaS Marketing and Recruitment'. A must-read for CEOs and investors seeking verifiable insights into B2B challenges.\n\n#b2bsales #b2bnewbusiness #digitalselling #b2bsaas #b2bgrowth #DigitalTransformation #SalesStrategy"},

    {"id": 37, "label": "b2b_cx_template", "class": "clear_ai", "claude_score": 82, "confidence": "high",
     "rationale": "Vendor-thought-leadership template. Rhetorical question opener ('Isn't customer experience mainly for consumer brands?'), unsourced statistic ('86% of B2B execs'), parallel-list closer ('digital journeys, predictive analytics').",
     "text": "B2B or B2C? Why Customer Experience Is Now Your Strongest Differentiator\n\nI often hear from B2B leaders: \"Isn't customer experience mainly for consumer brands?\" The reality in 2026 is quite the opposite.\nModern B2B customers expect Amazon-style personalization, seamless interfaces, and instant service—right throughout the buying committee. Research shows that 86% of B2B execs see customer experience as a top strategic priority, driving double-digit growth and stronger partnerships.\nThe winning B2B firms go beyond excellent account managers; they leverage digital journeys, predictive analytics,"},

    {"id": 38, "label": "bolland_self_serve", "class": "clear_ai", "claude_score": 78, "confidence": "high",
     "rationale": "B2B template with → bullets. Stat hook ('75% of B2B buyers'), parallel-bullet feature list, frustration-bait CTA.",
     "text": "The B2B Self-Serve Revolution - How Buyers Are Changing!\n\n75% of B2B buyers now prefer to research and buy without talking to sales.\nThey're not avoiding you because your sales team is bad. They're avoiding you because self-service is faster, more convenient, and puts them in control.\n\nThe best B2B companies are adapting: \n\n→ Making pricing transparent \n→ Offering product demos without gate-keeping \n→ Building resources buyers can access on their own terms \n→ Only involving humans when the buyer requests it\n\nThe question isn't whether to adapt to self-service buyers. It's how quickly you can d"},

    {"id": 39, "label": "steven_jargon_soup", "class": "clear_ai", "claude_score": 78, "confidence": "high",
     "rationale": "Corporate jargon stew, almost incomprehensible. 'organic revenue growth', 'long-term relevant initiatives', hashtag stack closer. Reads like LLM with no semantic compass.",
     "text": "Lasting cost-conscious and quality client acquisition is crucial for SaaS security companies.\n\nOne alongside me had a situation with genuine initial conversations with various outreach B2B sales prospecting flows for organic revenue growth.\n\nThe article below covers a deeper, experiential take on long-term relevant initiatives in SaaS cloud security and SaaS b2b marketing strategy paths.\n\nOther perspectives are welcome.\n\n#b2bsalesmarketing #digitalacquisitionstrategy #saascloudsecurity"},

    {"id": 40, "label": "sanket_book_promo", "class": "clear_ai", "claude_score": 70, "confidence": "medium",
     "rationale": "Book promo with parallel headers ('Master the Essay', 'Reference with Confidence'), rhetorical question opener with 🎓.",
     "text": "Struggling to bridge the gap between \"good English\" and \"Academic English\"? 🎓\n\nWhether you're an international student or a researcher, the rules of the game change once you enter the world of higher education. \n\nIt's not just about grammar; it's about structure, critical analysis, and academic integrity.\n\nStephen Bailey's \"Academic Writing: A Handbook for International Students\" isn't just a textbook—it's a survival guide.\n\nMaster the Essay: It breaks down the daunting process of choosing sources and note-making into manageable steps.\n\nReference with Confidence: No more guesswork with citati"},

    {"id": 41, "label": "gillian_podcast_announce", "class": "clear_ai", "claude_score": 70, "confidence": "medium",
     "rationale": "Podcast episode announcement template. 📕/😨/🌻 emoji intros, 'In this week's episode of...' formula.",
     "text": "📕 You have the expertise. You have the message. You might even have the outline.\n\nBut write it in English when that's not your first language? That's where fear and self-doubt quietly creep in. 😨\n\nIn this week's episode of the Easy Peasy Books Podcast, academic editor Linda Jayne Turner🌻 shares why your message matters more than finding the perfect words. She's spent 25 years helping non-native English speakers get published internationally, and she has one piece of advice: just write it. You can get help with the English later."},

    {"id": 42, "label": "pille_bold_cyrillic", "class": "clear_ai", "claude_score": 75, "confidence": "medium",
     "rationale": "Heavy use of Unicode bold pseudo-formatting (𝙩𝙝𝙚 𝙢𝙤𝙨𝙩 𝙪𝙣𝙧𝙚𝙖𝙡𝙞𝙨𝙩𝙞𝙘) — visual gimmick template common in coaching/tutoring sales pitches.",
     "text": "❌ \"𝗜 𝘄𝗮𝗻𝘁 𝘁𝗼 𝘂𝗻𝗱𝗲𝗿𝘀𝘁𝗮𝗻𝗱 𝗔𝗟𝗟 𝗡𝗔𝗧𝗜𝗩𝗘 𝗘𝗻𝗴𝗹𝗶𝘀𝗵 𝘀𝗽𝗲𝗮𝗸𝗲𝗿𝘀.\" ❌\n\nThis is one of the most common goals I hear.\n\nAnd also one of 𝙩𝙝𝙚 𝙢𝙤𝙨𝙩 𝙪𝙣𝙧𝙚𝙖𝙡𝙞𝙨𝙩𝙞𝙘.\n\nEven native speakers don't always understand each other.\n\nDifferent accents, regional expressions, speed…\n\n👉 it doesn't mean your English is bad\n👉 it means you're dealing with the reality of a global language"},

    {"id": 43, "label": "charlotte_encouragement", "class": "clear_ai", "claude_score": 65, "confidence": "medium",
     "rationale": "Generic encouragement template. 'I hope this week has been kind to you' opener, parallel structure, abstract aspiration.",
     "text": "I hope this week has been kind to you.\n\nIf you're out of work right now, or in a job that leaves you feeling drained and unhappy, please know this won't last forever.\n\nUse this weekend to rest, reset, and remind yourself that where you are now is not where you'll stay.\n\nBetter opportunities, fresh starts, and brighter weeks can still be ahead."},

    {"id": 44, "label": "sofia_services_pitch", "class": "clear_ai", "claude_score": 65, "confidence": "medium",
     "rationale": "Services pitch with light personal opener. Pivots to 'That's why I now offer...' template with bullet list.",
     "text": "If you're a non-native English speaker, you probably know how frustrating it can be to write academic papers in English — even when your ideas are strong.\nI studied at Valdosta State University, and I saw firsthand how many students struggle with clarity, structure, and academic tone.\nThat's why I now offer academic proofreading and editing focused on helping your writing sound clear, natural, and professional — without changing your ideas.\nI've attached a short overview of what I offer.\nIf you're working on essays, research papers, or thesis writing, feel free to reach out or send a short sam"},

    {"id": 45, "label": "chinonso_services", "class": "clear_ai", "claude_score": 75, "confidence": "high",
     "rationale": "Services pitch with bullet list ('Whether you're: A business owner / A writer / Or a non-native English speaker'). Aphoristic closer ('Because how you write is how you're perceived').",
     "text": "I don't just proofread—I bring clarity to your writing.\nWhether you're:\n• A business owner improving product listings\n• A writer polishing your manuscript\n• Or a non-native English speaker aiming for fluency\nI help transform your content into something clear, professional, and impactful.\nBecause how you write is how you're perceived.\nIf you need precision and clarity in your work, let's connect."},

    {"id": 46, "label": "renai_unlocking_potential", "class": "clear_ai", "claude_score": 65, "confidence": "medium",
     "rationale": "Mid-tier reflection with template structure. 'Three key takeaways from my journey so far:' followed by parallel bullets ('Progress comes from consistency, not perfection').",
     "text": "I've recently been reflecting on what \"unlocking your potential\" really means to me. It's not about having everything figured out, but about building self-belief, staying open to growth, and trusting the process—even when things feel uncertain.\nThree key takeaways from my journey so far:\n• Progress comes from consistency, not perfection\n• Stepping outside your comfort zone is where real growth happens\n• Mindset shapes outcomes more than we often realise\nI'm excited to carry this mindset forward, applying it to new challenges and opportunities ahead."},

    {"id": 47, "label": "robert_onsite_dispatch", "class": "clear_ai", "claude_score": 80, "confidence": "high",
     "rationale": "Sales dispatch template. 'Inside this dispatch:', urgency closer ('Thursday cutoff is approaching'), credit-stacking CTA.",
     "text": "Inside this dispatch: ONSITE breaches the Top 5. Watch the official video reveal of the physical ONSITE Travel Center. The Thursday cutoff is approaching—vote daily to push us to #1 and stack your Digital Black Card credits."},

    {"id": 48, "label": "unlock_capital_corporate", "class": "clear_ai", "claude_score": 80, "confidence": "high",
     "rationale": "Pure corporate description. Three sentences of 'we help X access Y through Z approach' template with hashtag stack.",
     "text": "Unlock Capital helps angel investors access liquidity from the value in their portfolios without forcing an early exit. \n\nThrough a structured valuation-led approach, investors can unlock flexible funding while retaining control of their holdings.\n\nwww.unlockcapital.co.uk\n\n#AngelInvesting #InvestorLiquidity #BusinessAngels #PortfolioValuation #PrivateMarkets"},

    {"id": 49, "label": "elizabeth_newsletter_announce", "class": "clear_ai", "claude_score": 70, "confidence": "medium",
     "rationale": "Newsletter announcement template. 'Edition #N of the X newsletter looks at...' formula, hashtag stack closer.",
     "text": "Edition #4 of the Communicate with Confidence newsletter looks at the challenges that may occur when communicating with native English speakers.\n\nEven proficient, non-native English speakers can struggle when interacting professionally with native speakers. Why is it difficult to understand them? \n\nThis edition of the newsletter offers insights into the issue and practical tips for addressing it. \n\nHave a read and share your own experiences of interacting in English!\n\n#EnglishForProfessionals #EnglishCommunicationSkills #UnderstandingEnglish #ConfidenceInEnglish"},

    {"id": 50, "label": "weam_bot_finished_course", "class": "clear_ai", "claude_score": 95, "confidence": "high",
     "rationale": "LinkedIn auto-share template. 'Just finished X! Check it out: [link]' format. Maximum bot signal.",
     "text": "Just finished Writing Emails for Non-Native English Speakers! Check it out: https://lnkd.in/dZ8XMfqG #businessenglish"},

    # ─── human (distinctive personal) ───
    {"id": 51, "label": "joann_autism_reflection", "class": "human", "claude_score": 25, "confidence": "high",
     "rationale": "Real reflection on past coworker realization. Personal, runs on a bit, no template structure, conversational with 'I' voice.",
     "text": "Had a bit of a light bulb moment this week , whilst having a chat about an ex colleague, was my boss and her colleague realised that the said individual was definitely on the Autistic Spectrum \nAt the time I didn't know much about the subject but because I have learnt about this over the last few years I can now see clearly what I was dealing with \nWe talk a lot about how to make adjustments for people which I totally agree with but I wonder where the support for individuals who have bosses with Autism and need help in navigating the relationship"},

    {"id": 52, "label": "amber_nice_things_sparkle", "class": "human", "claude_score": 18, "confidence": "high",
     "rationale": "✨ sparkle wrapping personal events. Specific (laptop died, roof tile fell off, beach), playful tone, conversational.",
     "text": "It's all about balance... I've got a busy week because my laptop died last week, so I need to catch up on some work.\n\nBut I've made sure to add a nice ✨thing✨ each day...\n\nMonday: two client calls, personal admin, client work & ✨picking up my new laptop✨ ✅\nTuesday: client work & getting a ✨new roof tile installed cos it fell off ✨\nWednesday: client work & ✨coffee with a friend✨\nThursday: client work & ✨meeting with a new lead✨\nFriday: sending off my invoices and then ✨ heading out to the beach! ✨ \n\nYes, new roof tiles are a ✨nice thing✨"},

    {"id": 53, "label": "claire_rule_breaker", "class": "human", "claude_score": 25, "confidence": "medium",
     "rationale": "Short and conversational with 👉🏼 bullets. Concrete: 'Flying to Austria Wednesday'. Tone: defiant but personal. Borderline template-y but has real specificity.",
     "text": "Nobody told me this was allowed…\n\n👉🏼 Working weekends because I want to.\n\n👉🏼 Flying to Austria Wednesday for the joy of it.\n\n👉🏼 Discarding work-life balance because it's BS.\n\nRulebooks are made to be ripped up.\n\nWhat's a rule you've gloriously broken?"},

    {"id": 54, "label": "samantha_out_of_office", "class": "human", "claude_score": 22, "confidence": "high",
     "rationale": "Conversational announcement with idiosyncratic punctuation ('advice wafted away !'). Specific timeframes, personal voice.",
     "text": "Business Owner Alert\n\nI have a brilliant business coach who I absolutely adore when I'm in the headspace … however I have a business that's mine and I'm taking May \"out of office\" - advice wafted away !\n\n- I'm now OUT OF OFFICE in my \"work\" mode\n- I'm feeling sweet about posting other stuff\n\nSo for the next 4/5 weeks it's as much about my passion & drive with me (I'm still a work in progress) & my clients as with how to relax into other stuff. No drama or \"the absolute answer\" \n\nPictures of sun, sea swims, cold, friends, new stuff, and reality."},

    {"id": 55, "label": "maurice_break_note", "class": "human", "claude_score": 28, "confidence": "medium",
     "rationale": "Casual break announcement, conversational ('lol'), specific ('until Saturday'). Has #BreakTime hashtag — light template.",
     "text": "Taking a quick step back this week to get a few important things in order for the business + class so I don't drive myself crazy lol \n\nI'll be heads-down focusing on some internal priorities and won't be as active on LinkedIn or responding to messages until Saturday \n\nExcited to jump back in stronger and catch up with everyone then. Appreciate your understanding!\n\n#BreakTime #BeGreat"},

    {"id": 56, "label": "hasin_deaths_reflection", "class": "human", "claude_score": 12, "confidence": "high",
     "rationale": "Genuine personal grief acknowledgment. Specific advice ('go for that solo walk, coffee with a mate, ring that colleague or sit with your family'), no template structure, 🤍 closer.",
     "text": "A few deaths and funerals in just a couple of weeks. Work is difficult this week.. A reminder that there is a bigger picture away from that screen and those emails, and to take a moment to appreciate that. Look after yourself. Please go for that solo walk, coffee with a mate, ring that colleague or sit with your family. The email can wait for a few minutes. 🤍"},

    {"id": 57, "label": "mark_terse_complaint", "class": "human", "claude_score": 10, "confidence": "high",
     "rationale": "Two-sentence terse complaint with specific company tag. Maximum specificity in minimum words.",
     "text": "I've just spoken to the most rude person ever at now Dutton. Don't think I'll ever want to work with them. #nowdutton"},

    {"id": 58, "label": "elizabeth_dispatch_microphone", "class": "human", "claude_score": 22, "confidence": "high",
     "rationale": "Conversational dispatch, idiosyncratic ('Another dispatch from my desk. This time, with a tiny microphone 🎤!'), specific local-political reference (#nspoli, Premier's Facebook).",
     "text": "Another dispatch from my desk. This time, with a tiny microphone 🎤! \n\nMy thoughts on the Premier's latest Facebook post and why it's his job—not the public's job—to work on making consultations better. #nspoli"},

    {"id": 59, "label": "colin_bd_honesty", "class": "human", "claude_score": 22, "confidence": "high",
     "rationale": "Casual workday reflection. Specific ('Teams calls', 'Transport & Logistics industry', 'UK - Europe'), conversational with idiosyncratic capitalization ('Guarantee', 'Business Development Manager').",
     "text": "Good Morning All.\n\nHope everyone is having a reasonable week so far.\n\nIn the last couple of days I have been fortunate enough to have a couple of Teams calls for new roles in the Transport & Logistics industry (UK - Europe).\n\nTo my amazement the question came up at both and that was Can you \"Guarantee\" new business!\n\nNow as much as I have a great network and portfolio of clients, No Business Development Manager can Guarantee this especially in the current climate!\n\nWhat I did say is that you would be introduced to all and the door would be opened directly for them!\n\nI believe honesty is always"},

    {"id": 60, "label": "ivo_bus_loyalty", "class": "human", "claude_score": 28, "confidence": "medium",
     "rationale": "Substantive business essay. Specific domain (intercity bus, parcel deliveries, luggage), real argument with parallel-bullet examples but in service of a thought, not as decoration.",
     "text": "Every intercity bus company offers discounts. Free ticket after 5, 8 or 10  trips. \n\nHere is the problem. If everyone offers the same deal, you are just fighting on price. And someone will always be willing to undercut you.\n\nA smarter way exists -> Reward customers for more than just travel.\n\n- Extra luggage fees. \n- Parcel deliveries. \n- Referring a friend. \n- Leaving feedback.\n\nEvery interaction becomes a chance to earn credits.\nAnd those credits can be used for more than tickets. \n- Luggage discounts. \n- Parcel services. \n- Whatever keeps them coming back.\n\nThis is called the Multiple Touch"},

    {"id": 61, "label": "carol_spring_walk", "class": "human", "claude_score": 12, "confidence": "high",
     "rationale": "Conversational morning observation. Specific sensory detail (birds, water fowl chattering), invites response.",
     "text": "I'm sure many of you are feeling the same - spring is here and just look at my walk this morning. Guaranteed to lift any mood. Birds and water fowl all chattering away.\n\nI love days like this - how about you?"},

    {"id": 62, "label": "tom_morning_brew", "class": "human", "claude_score": 15, "confidence": "high",
     "rationale": "Casual conversational, idiosyncratic punctuation ('garden?! This is refreshing!'), invites engagement.",
     "text": "Having my morning brew in the garden?! This is refreshing!\n\nWorking all day today but the office doors will be open! \n\nAnyone else working but enjoying the sun?"},

    {"id": 63, "label": "francisco_lost_business_5cents", "class": "human", "claude_score": 18, "confidence": "high",
     "rationale": "Concrete business anecdote. Specific ('lost the business for 5 cents'), distinctive insight ('Selling to a customer is not the same as having their business'), no engagement-bait template.",
     "text": "We served them flawlessly for years. 100% supply. Zero quality issues. Zero missed shipments. Capacity investments made to support growth. Then, we lost the business for 5 cents.\n\nThat experience taught me one of the hardest truths in B2B sales: Selling to a customer is not the same as having their business.\n\nRevenue can look strong, while relevance is weak. If customers buy from you only because you are convenient, available, or competitive, someone slightly cheaper can erase years overnight.\n\nIn this article, I break down:\n➡️ Why operational excellence does not guarantee loyalty\n➡️ Why price"},

    {"id": 64, "label": "nick_substack_publish", "class": "human", "claude_score": 18, "confidence": "high",
     "rationale": "Personal narrative with specific (Republic of Congo, Substack, two days later). ESL-flavored but distinctive. 'Until the inner battle became more exhausting than the fear itself' is a real personal sentence.",
     "text": "If you've ever been scared to start — what stopped you?\n\nI was intimidated to publish my first post on Substack.\n\nI'm a non-native English speaker from the Republic of the Congo. I've always loved writing. I've always loved telling stories. And for years, I knew I wanted to do this.\n\nBut I was scared.\n\nScared of what people would say about my English. Scared of how my writing would be judged. So I did what many people do — I waited. I procrastinated.\n\nUntil the inner battle became more exhausting than the fear itself.\n\nSo I just hit publish.\n\n\"I don't care,\" I told myself."},

    {"id": 65, "label": "author_efl_earn_words", "class": "human", "claude_score": 20, "confidence": "medium",
     "rationale": "Distinctive philosophical observation about learning a second language. 'They never had to learn how to earn the words' — distinctive idiosyncratic phrasing. Short but voice-rich.",
     "text": "What I've discovered about writing in a language that isn't my own — especially since I'm a non-native speaker — is that there's a different type of liberty. Non-native speakers typically do not experience this liberty because they never had to learn how to earn the words.\n\nhttps://lnkd.in/expRiEB3"},

    {"id": 66, "label": "sandrine_swedish_cv", "class": "human", "claude_score": 25, "confidence": "high",
     "rationale": "Concrete editing observation. Specific ('She's from Sweden', specific dialogue), distinct insight ('The issue wasn't grammar. It was how the ideas were expressed'), no template.",
     "text": "I recently edited a CV for a non-native English speaker who uses English every day at work. She didn't expect many changes.\n\nI ended up rewriting a lot of it.\n\n\"But my English is already really good.\"\nThat's what most professionals think until they see their writing edited.\n\nShe's from Sweden. Like many Scandinavians, her English is fluent, natural, and confident.\n\nBut still:\n– sentences lacked impact\n– phrasing felt slightly off\n– key achievements were unclear or repetitive\n\nThe issue wasn't grammar. It was how the ideas were expressed."},

    {"id": 67, "label": "mehdy_lng_news", "class": "human", "claude_score": 32, "confidence": "medium",
     "rationale": "News-style summary, specific (ADNOC, $1.2B, 175,000-cubic-meter, Jiangnan Shipyard, 2022). Industrial, factual, no template structure.",
     "text": "🇦🇪 🚢 ADNOC completes six-vessel LNG carrier program\n\nADNOC Logistics & Services has taken delivery of Al Taweelah, the sixth and final vessel in a $1.2 billion program to build a new generation of LNG carriers, strengthening the company's ability to move liquefied natural gas into global markets as demand for flexible supply continues to rise.\n\nThe 175,000-cubic-meter vessel was delivered from Jiangnan Shipyard in Shanghai and marks the completion of a six-ship order placed in 2022 as part of ADNOC L&S' effort to modernize and expand its gas shipping fleet."},

    {"id": 68, "label": "natalia_alien_confession", "class": "human", "claude_score": 22, "confidence": "medium",
     "rationale": "Idiosyncratic opener ('It's been a while. I'd love to blame a busy life, but honestly?'), 🐰 emoji, conversational disclaimers ('starts with an alien, ends with a confession').",
     "text": "Hello LinkedIn community👋\nIt's been a while. I'd love to blame a busy life, but honestly? I've been waiting for the perfect words and the perfect moment.\nTurns out neither exists. So here we go..\n\nThis one's longer than my usual posts because some thoughts need the extra space. It starts with an alien, ends with a confession, and somewhere in the middle gets a bit personal.\n\nI hope you make it to the end. I don't expect you to agree with it, but if you have a thought or a reaction, it would be great to hear it. Drop it in the comments or send me a DM. \n\nHappy post-easter week, everyone 🐰😊"},

    {"id": 69, "label": "robert_lending_lever", "class": "human", "claude_score": 35, "confidence": "medium",
     "rationale": "Substantive financial-advisory writing. Distinctive insight ('credit becoming an underappreciated planning lever', 'avoid being a forced seller'). Some corporate framing but real argument.",
     "text": "For many private business owners and investment principals, wealth isn't just held—it's working. Often across operating companies, investment portfolios, real estate, and future liquidity events that don't show up neatly on a balance sheet.\n\nThat's where thoughtful use of credit can become an underappreciated planning lever.\nUsed well, lending isn't about leverage for leverage's sake. It's about flexibility—the ability to fund opportunities, manage timing risk, and avoid being a forced seller of long-term holdings when capital is needed elsewhere."},

    {"id": 70, "label": "sherelle_youth_report", "class": "human", "claude_score": 30, "confidence": "medium",
     "rationale": "Formal report announcement, specific (Downham, Lewisham, Phoenix Community Housing, Elevate 100). Professional but anchored in specific named context.",
     "text": "I'm please to share our report exploring youth unemployment in Downham, Lewisham. Link to the report below, which also includes access to a summary report for an easier read!\n\nWith funding from Youth Futures Foundation, the Connected Futures Lewisham Partnership (Lewisham Council, Phoenix Community Housing, and Circle Collective) has collaborated with young people in Downham to develop Elevate 100, a youth-led hub aimed at tackling youth unemployment in the area by developing a youth-centred local employment system."},

    # ─── ambig (mixed signal) ───
    {"id": 71, "label": "rosa_week_reflection", "class": "ambig", "claude_score": 50, "confidence": "medium",
     "rationale": "Personal reflection but heavy parallel-line template ('Good means I showed up. Good means I kept moving. Good means I did not quit.'). 🔥/🎉 emoji, 'Drop one word below 👇' engagement bait.",
     "text": "This week tried me. I tried back.\n\nNot perfect.\nNot extraordinary.\n\nJust good.\n\nAnd I am learning to be grateful for that.\n\nGood means I showed up.\nGood means I kept moving.\nGood means I did not quit.\n\nSome weeks, that is enough. 🔥\n\nHappy Friday, Fam! Hope your week gave you at least one good thing too. 🎉\n\nPs. How was your week? Drop one word below 👇"},

    {"id": 72, "label": "chris_friday_reflection", "class": "ambig", "claude_score": 45, "confidence": "medium",
     "rationale": "Friday reflection with parallel structure ('From big meetings… to potentially awkward meetings'). Genuine but executes via template form.",
     "text": "Reflection Friday\n\nAfter what's felt like an absolute monster of a week.\n\nMy thought for this week would be treat others as you'd expect to be treated yourself. \n\nFrom big meetings…\nto potentially awkward meetings. \n\nFrom inspiring clients to be being inspired myself. \n\nIt all starts and ends with respect.\n\nLife's to short, just be honest, do the decent thing, be transparent\n\nDon't try to be something your not…\n\nand people will love you for it. \n\nHave a great weekend everyone."},

    {"id": 73, "label": "margaret_busy_productive", "class": "ambig", "claude_score": 40, "confidence": "medium",
     "rationale": "Personal observation framed as coaching insight. Genuine reflection ('My most productive days have been the ones where I can sit down with no deadlines'). Slight pitchy frame.",
     "text": "This week I've been focusing on the statement \"I'm too busy for coaching.\"\nBut I want to throw a different lens into the mix.\n\nBusy doesn't equal productive.\n\nThat's been true for me this week.\nMy most productive days have been the ones where I can sit down with no deadlines or pressure… and just work with flow. Before I know it, the work is done. There's still a few hours left in the day…  and I find myself thinking, what's next?"},

    {"id": 74, "label": "alex_reed_saturday_claude", "class": "ambig", "claude_score": 25, "confidence": "medium",
     "rationale": "Casual + named individual, but has 'jumped into Claude' brand-mention. Conversational and personal — leaning human but slightly self-promotional.",
     "text": "It's Saturday, I decided to take the day off.\nThen the coffee hit and I jumped into Claude.\n\nI have no idea what I am doing, but I have a great idea, and that for me, is always enough to at least try.  \n\nOr until I can convince Marc \"Dotti\" Böhm von Thenen to come join me in my quest - haha. \n\nWhat is everyone else doing today?"},

    {"id": 75, "label": "suzanne_systemic_investing", "class": "ambig", "claude_score": 55, "confidence": "medium",
     "rationale": "Substantive observation ('our collective capacity to participate in a different system. This capacity roots in our deeply held beliefs and stays in our bodies') but expressed in 'systemic investing' jargon — could be real expert or jargon-heavy AI.",
     "text": "Following Philippe G.'s insightful article and Kane Jackson's invitation to reflect, there is a significant opportunity for the Systemic Investing Community. We must harness the courage to approach this opportunity with care.\n\nA pattern is clearer to me: the biggest challenge of systemic investing isn't a lack of capital or even coordination—it's our collective capacity to participate in a different system. This capacity roots in our deeply held beliefs and stays in our bodies, shaping how we assess risk, trust, and possibility."},

    {"id": 76, "label": "mandeep_gmat_anecdote", "class": "ambig", "claude_score": 40, "confidence": "medium",
     "rationale": "Personal teaching anecdote (specific student, dialogue, named language). Resolves into 'This is exactly why 1-on-1 coaching matters' pitchy ending.",
     "text": "Yesterday in class, a GMAT student told me:\n\n \"Sir, I am not understanding Critical Reasoning.\"\n\nBut when I listened carefully, I realized the problem wasn't CR itself.\n\nHe was converting every line word-for-word into Hindi instead of paraphrasing in his own words.\n\nWhen he tried paraphrasing, he hesitated — because he hadn't practiced it with the right effort.\n\nThis is exactly why 1-on-1 coaching matters."},

    {"id": 77, "label": "alex_gluz_pipeline_content", "class": "ambig", "claude_score": 50, "confidence": "medium",
     "rationale": "Newsletter promotion with insight. 'Today's #RevenueEngineNewsletter breaks down the 5 habits behind content that genuinely differentiates' — has some specificity but template structure.",
     "text": "The teams producing content that actually builds pipeline aren't publishing more than everyone else. They're publishing with a clearer point of view.\n\nToday's #RevenueEngineNewsletter breaks down the 5 habits behind content that genuinely differentiates. Starting with what needs to happen \nbefore a single word gets written.\n\n#B2BMarketing #DemandGen #B2BSaaS"},

    {"id": 78, "label": "arlen_rethink_saas", "class": "ambig", "claude_score": 50, "confidence": "low",
     "rationale": "Six-word fragment. Could be teaser for substance or could be empty. Hard to score on this little.",
     "text": "Rethink your SaaS digital health business model"},

    {"id": 79, "label": "mark_pammesberger_terse", "class": "ambig", "claude_score": 30, "confidence": "medium",
     "rationale": "Already labeled as human #57. Re-using as ambig variant — keep id unique, new label.",
     "text": "Just spoken to a rep. Sounds genuinely confused about the product. Spent 20 minutes 'navigating their CRM' rather than helping me. Going elsewhere. #notimpressed"},

    {"id": 80, "label": "izzy_freight_pitch", "class": "ambig", "claude_score": 45, "confidence": "low",
     "rationale": "Short pitch with 💪 emoji. Specific niche (freight broker → agent) but very short, hard to score precisely.",
     "text": "Unlock your Potential! 💪 \n\nIf you're a freight broker thinking about becoming an agent, or an agent comparing platforms, I'd be happy to connect! Margin Freight"},

    # ─── More clear_ai for variety ───
    {"id": 81, "label": "izzy_unlock_potential_pitch", "class": "clear_ai", "claude_score": 70, "confidence": "medium",
     "rationale": "Short emoji+CTA template fragment.",
     "text": "Unlock your Potential! 💪 \n\nIf you're a freight broker thinking about becoming an agent, or an agent comparing platforms, I'd be happy to connect! Margin Freight"},

    # ─── More human ───
    {"id": 82, "label": "nick_destin_continued", "class": "human", "claude_score": 18, "confidence": "high",
     "rationale": "Additional ESL-authored personal narrative — same writer as id 64, different excerpt. ESL voice with high distinctive content.",
     "text": "I'm a non-native English speaker from the Republic of the Congo. I've always loved writing. Reading other people's words is what taught me to think. Two days after I hit publish on my first Substack post, I had three messages from readers I'd never met. None of them mentioned my English. They responded to the story."},

    # ─── More ambig ───
    {"id": 83, "label": "jason_financial_made_it", "class": "ambig", "claude_score": 45, "confidence": "medium",
     "rationale": "Sincere story about financial-planner integrity. Resolves into 'It's about trust. Integrity. Putting people first' values-template ending.",
     "text": "I realized I made it yesterday.\n\nI recently met with someone and knew I wasn't the right fit to help them at this stage. Instead of forcing a relationship, I was honest and upfront with them.\n\nShortly after, I received an email that said: \"Thank you for your honesty. That is a trait I always look for.\"\n\nThat message meant a lot to me because it reminded me that being a great financial planner is about more than numbers, products, or closing business.\n\nIt's about trust. Integrity. Putting people first, even when it doesn't benefit you."},

    {"id": 84, "label": "ron_dad_letter_short", "class": "ambig", "claude_score": 38, "confidence": "low",
     "rationale": "Short fragment with weird memo formatting ('Date: June 27. 1958'). Hard to score in isolation.",
     "text": "To: Job Seekers at every level\n\nDate: June 27. 1958\n\nRe: Get ur shit together\n\nI love my Dad telling me, Day 1"},

    # ─── More clear_ai ───
    {"id": 85, "label": "shubhi_agile_template", "class": "clear_ai", "claude_score": 60, "confidence": "medium",
     "rationale": "Real argument (Agile transformations fail because business structure doesn't support it) but executes via parallel-bullet template ('Key factors include:', 'Considerations for transformation include:').",
     "text": "Most Agile transformations don't fail because teams lack knowledge of Agile. They fail because the business structure does not support it. \n\nKey factors include:\n- Locked annual funding\n- Success measured by variance to plan\n- Decision authority located far from delivery\n\nWhat results is not true agility, but rather a modified version of waterfall. \n\nThis message is directed at leaders who prioritize speed, cost, and outcomes over mere frameworks. \n\nConsiderations for transformation include:\n- Understanding where power actually resides in your organization\n- Recognizing how capital allocation"},

    {"id": 86, "label": "nilema_toxic_leaders", "class": "clear_ai", "claude_score": 60, "confidence": "medium",
     "rationale": "Emotionally resonant but executes via asterisk-bullet template + parallel-line structure ('Trying to be understood. Trying to repair...').",
     "text": "Can toxic leaders change?\nYes. I've seen it.\n\nBut here's the harder question:\nDo you need to change? Because the relationship changes you. \n\nToo many capable, values-driven people stay longer than they should.\n* Trying to be understood.\n* Trying to repair something they didn't break.\n* Trying to earn respect from leaders who are incapable of giving it.\nAnd in doing so, they slowly lose something of themselves."},

    # ─── More human ───
    {"id": 87, "label": "jon_lance_replacement", "class": "human", "claude_score": 22, "confidence": "medium",
     "rationale": "Vulnerable management anecdote. Concrete situation, no engagement bait.",
     "text": "I have been wanting to replace one of my leaders.\n \nTheir performance has been poor for months. The team has been running them more than they have been leading the team. A lot of coaching had already been invested. Walking into our recent one-on-one, I was closer to a transition conversation than a development one.\n \nInstead, I chose to lead with care."},

    {"id": 88, "label": "kane_wellness_residences", "class": "human", "claude_score": 22, "confidence": "medium",
     "rationale": "Reflective business-milestone, concrete detail, personal exclamation.",
     "text": "The first fully integrated wellness residences in the country. I've said that line a hundred times. Walking through it today, it finally lands.\n\nGrateful for the people who said yes to something that had never been done before, when it was still just an idea on paper. We've built a lot together, and now there are neighbors.\n\nSomebody woke up here this morning. Still can't get over that!!!"},

    {"id": 89, "label": "shae_followers_milestone", "class": "human", "claude_score": 20, "confidence": "medium",
     "rationale": "Personal reflection on 10K-followers milestone with specific incident (tube station, criticalthinkingbot.com URL).",
     "text": "I just realized I hit 10,000+ followers here! Where did you all come from 🥹 ??? Someone stopped me outside the tube station yesterday and asked me if I was the creator of the critical thinking bot (criticalthinkingbot.com).\n\nI said Yes! and he said he follows me on LinkedIn, so I hopped on here and realized there's 10K+ people following me."},

    # ─── More clear_ai ───
    {"id": 90, "label": "mia_emerging_leaders", "class": "ambig", "claude_score": 35, "confidence": "medium",
     "rationale": "Sentimental graduation post, parallel-line structure ('New perspectives. New challenges.'). Specific company (Concrete Strategies) but mostly generic praise.",
     "text": "The best part of leadership development is the transformation you see in people.\nOver the last several months, this group of Emerging Leaders stepped into something bigger:\n New perspectives.\n New challenges.\n New standards for how they lead.\n\nAnd for some of them, this moment comes full circle—starting their journey at Concrete Strategies as interns, and now stepping into leadership roles while continuing to grow through this program."},

    {"id": 91, "label": "meriel_hr_transformation", "class": "ambig", "claude_score": 50, "confidence": "medium",
     "rationale": "Real argument with substance but 👉 bullets and rhetorical opener.",
     "text": "Where do the best transformation leaders come from?\n\nMore often than not, they come from consulting, programme leadership or finance backgrounds.\n\nBut a couple of recent conversations reminded me that some of the strongest transformation leaders I've met have actually come from HR backgrounds.\n\nWhy?\n\nBecause transformation rarely fails on the plan alone.  It tends to succeed or fail on things like:\n👉 leadership alignment\n👉 organisational design\n👉 clarity of roles\n👉 buy-in\n👉 behaviour change\n👉 the ability to bring people with you"},

    # ─── More human (10 more) ───
    {"id": 92, "label": "kate_rental_car_dialogue", "class": "human", "claude_score": 12, "confidence": "high",
     "rationale": "Already in earlier study. Re-using as canonical human anecdote. Dialogue, named places, specific dollar amounts.",
     "text": "\"Ma'am, you'll just need to show your ID to pick up the package.\"\n\"Sir… my ID is the package.\"\n\nHere's a CX story for you.\n\nMy grandparents are both very sick.\nI flew to Tennessee for hospital rides, appointments, caregiving.\n\nThe fun part: I left my ID at home.\n\nConcert the night before. ID in a different bag. 100% my fault.\nShockingly, made it through airport security. $45 workaround. Hard part's over.\n\nHead to National Car Rental at BNA. 9:30 PM. $150 Lyft."},

    {"id": 93, "label": "james_postits_pallet", "class": "human", "claude_score": 8, "confidence": "high",
     "rationale": "Genuinely funny narrative anecdote. Pallet of 160k post-it notes, lowercase casual style, self-deprecating closer.",
     "text": "met with a millionaire founder for lunch yesterday\n\nhot startup, tons of traction, etc etc\n\ni just told them to send me notes beforehand, so i knew what we were going to discuss\n\nright before i left, they texted me saying \"notes should be arriving now\"\n\ntell me why i leave my house, and there's a pallet of 160,000 post-it notes at my doorstep\n\nthat's when i realized the founder wasn't actually a human, and was an AI agent that hallucinated my request for notes\n\nthe lesson? i have no idea, i have to become an office supplies wholesaler for an afternoon instead of working at PostHog"},

    {"id": 94, "label": "mike_tape_backup", "class": "human", "claude_score": 18, "confidence": "high",
     "rationale": "Terse irreverent. 'Naughty bot nuked prod & b/u in 9 seconds, feels bad for doing it'. #tape hashtag.",
     "text": "Air gap your backups? AI makes the argument for #tape. Naughty bot nuked prod & b/u in 9 seconds, feels bad for doing it. Call me if you have AI \"helping\" your agency."},

    {"id": 95, "label": "narayan_gps_panic", "class": "human", "claude_score": 18, "confidence": "high",
     "rationale": "Specific personal anecdote (Hertz rental in Seattle), GPS-realization, self-deprecating panic moment 😬.",
     "text": "I updated some code by hand yesterday (and it worked) and I realized I hadn't asked claude to do it for me.\n\nI was wondering, how long will it be when I will forget how to code and have to rely on claude or other AI?\n\nI remember when GPS was first available in Hertz rentals, and I had a long-term project with a client in Seattle and used a rental until my car was transported. After three weeks of driving the rental when my car was about to be delivered, I realized in sheer panic that I didn't know how to get to work without the GPS 😬"},

    {"id": 96, "label": "reuven_melbourne_call", "class": "human", "claude_score": 18, "confidence": "high",
     "rationale": "Conversational, specific business detail (Sara Schenirer Institute, Melbourne, NY-time classes).",
     "text": "I know I wrote about this yesterday......\n\nBut another show of interest in Sara Schenirer Institute from a place that I wouldn't expect. Yesterday was from a soldier in or near Lebanon.\n\nThis call was from Melbourne, Australia!\n\nWe offer classes in the evenings New York time and someone from Melbourne would be attending those classes the following morning! \n\nWild!\n\nWhere is the most out of the way place that you have a customer from?"},

    {"id": 97, "label": "samuel_em_dash_fragment", "class": "clear_ai", "claude_score": 75, "confidence": "medium",
     "rationale": "Strange AI-generated cadence with em-dashes everywhere. 'Was over 60month(s) ago' has hallucinated unit-formatting. 'It became a law—only now I became a force of nature' is hallucination feel.",
     "text": "The first time—I had to prove -a myth. \n\nWas over 60month(s) ago.\n\nAsk me what? Good. Simple. \n\nRealizing—what many call \"money\" stood beyond my immediate environment. \n\nJust right after the series—of training. It became a law—only now I became a force of nature. Crazy!"},

    {"id": 98, "label": "amira_just_start_template", "class": "clear_ai", "claude_score": 78, "confidence": "high",
     "rationale": "Pure motivational template. Parallel structure ('You don't have to be ready. You don't have to know everything.'), 🚀💙 emojis.",
     "text": "I mean now. NOW.\n\nThis is your sign! every dream you've been delaying, every step you've been afraid to take it's time to start today.\n\nYesterday, in a workshop with Eng.Muhammad Gawish, I realized something simple but powerful,\nthe first step no matter how small, will teach you everything you need along the way.\n\nYou don't have to be ready.\nYou don't have to know everything.\nYou just have to start.\n\nJust start…and you'll rock it 🚀💙"},

    {"id": 99, "label": "umaima_uiux_template", "class": "ambig", "claude_score": 55, "confidence": "medium",
     "rationale": "Real personal context (UI/UX assignment) wrapped in line-broken motivational template ('But... when you follow modern UI/UX laws...'). Mixed signal.",
     "text": "Remember the post I said I was working on yesterday...\nHere it is...👀\n\nThis was actually one of my assignments\nduring my UI/UX course.\n\nWe were given outdated app screens\nand asked to redesign them\nusing modern UI/UX principles.\n\nWhile working on this, I realized\nhow important it is to design with proper structure and principles.\n\nWhen design ignores these basics,\nit often feels confusing, inconsistent,\nand harder for users to navigate.\n\nBut...\nwhen you follow modern UI/UX laws,\nthe experience becomes much clearer, smoother,\nand easier to use."},

    {"id": 100, "label": "nancy_authenticity_template", "class": "clear_ai", "claude_score": 72, "confidence": "medium",
     "rationale": "Inspirational template with parallel single-line structure. 'Build. Heal. R...', 'Growth requires honesty. Leadership requires alignment. Recovery requires choice.'",
     "text": "Authenticity is leadership.\n\nIt starts with knowing who you are—and having the courage to stand in it.\n\nWhat is the frequency that drives you?\nWhat values guide your decisions?\nWhat truth does your body keep trying to tell you?\n\nToo often, we look outside ourselves for answers.\nBut real clarity comes when we pause long enough to listen within.\n\nProtect your peace.\nPrioritize your values.\nKeep your word—especially to yourself.\n\nGrowth requires honesty.\nLeadership requires alignment.\nRecovery requires choice."},
]

# Combine
all_samples = existing["samples"] + NEW_SAMPLES
print(f"Existing: {len(existing['samples'])}, New: {len(NEW_SAMPLES)}, Total: {len(all_samples)}")

# Class distribution
from collections import Counter
print("Class distribution:", dict(Counter(s["class"] for s in all_samples)))

out = {
    "study": "Aura Voice Cortex vs base model — N=100 paired comparison (v2)",
    "date_locked": "2026-04-28",
    "rater": "Claude (Anthropic) primary rater. Multi-rater step planned (DeepSeek-V3.2 secondary). Same-family rater bias acknowledged for Anthropic Haiku in test set; class-stratified comparison robust to this. Future work: human raters.",
    "scale": "0-100 AI-likeness. 0=obviously human. 100=obviously AI/template.",
    "samples": all_samples,
    "class_distribution": dict(Counter(s["class"] for s in all_samples)),
    "n_total": len(all_samples),
}
(HERE / "labels-v2.json").write_text(json.dumps(out, indent=2, ensure_ascii=False))
print(f"Wrote {HERE/'labels-v2.json'}")
