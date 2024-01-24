# Full-Stack-Chatbot-Application-Vector-DB-Integration-for-Enhanced-Prompts
Chatbot Application for WWGS Ecommerce! 

- Engineered an automated web scraper to collect e-commerce data, integrating with a Pinecone vector database for efficient data storage and retrieval.

- Implemented advanced retrieval algorithms using NLP and vector embeddings, significantly enhancing the chatbot's accuracy in providing hyper-relevant responses using prompt 
  contextualization with Open AI’s ChatGPT LLM API.

- Deployed scraper on AWS Lambda for automated, periodic updates
  
- Developed a responsive chatbot interface using Flask + HTML/CSS/Javascript

Application UI:
![image](https://github.com/vishnuvvaradhan/Full-Stack-Chatbot-Application-Vector-DB-Integration-for-Enhanced-Prompts/assets/144381362/b0f278a3-336d-46fa-883f-9faf1f686dc5)


Example of Enhanced Prompt on Backend: 

Closed Prompt: ['0.31: SkyTrak Personal Launch Monitor w/ Basic Practice Range Package: Black Product Price: 1995', '0.25: Optishot Optishot2 Golf Simulator: Additionally, we offer a 30-day warranty from date of purchase on the Golf Mat, Net, USB Cable, Tees, Tee Gripper, Foam Balls, and Turf. Product Color or Size - (if number): None Product Price: 500', '0.23: Optishot Golf In A Box 1 Golf Simulator: Additionally, we offer a 30-day warranty from date of purchase on the Golf Mat, Net, USB Cable, Tees, Tee Gripper, Foam Balls, and Turf. Product Color or Size - (if number): None Product Price: 1000', "0.22: SkyTrak Golf Simulator Studio Package: Deep\xa0- 13' (W) X 10' (H) X 10' (D) **Although this product may fit in your space, please make sure to take some practice swings to make sure you are comfortable swinging in your designated space. What's Included:  SkyTrak Launch Monitor  USB Cable USB Splitter Cable Quick Start Guide Product Information Guide SkyTrak App Virtual Driving Range    One Year of a SkyTrak Play & Improve Plan:   15 courses on WGT by TOPGOLF (IOS) 15 courses on TruGolf E6 Connect (IOS/PC)  Simulator Studio:  Studio Enclosure Optoma GT2000 HDR Projector Projector Mounting Arm Premium HDMI cable 5x5 Hitting Mat Putting Turf Ball Tray Enclosure Side Netting Product Color or Size - (if number): 10' Product Price: 5995", "0.22: SkyTrak SkyTrak+ Launch Monitor: What's Included:SkyTrak+ Launch MonitorSkyTrak SoftwarePower Cables & BrickChargerQuick Start Guide & User Manual Product Color or Size - (if number): None Product Price: 2995", '0.21: Voice Caddie SC4 Simulator + Launch Monitor: Product Color or Size - (if number): Black Product Price: 549.99', "0.19: Optishot Golf In A Box 5 Golf Simulator: The high dense foam and high quality turf delivers the lifelike golf experience right in your home. Size: 4'(L) x 5'(W)PROJECTORThe Golf In A Box 5 includes a high-quality, high-definition short-throw projector creating a real golf like atmosphere. Choose between a ceiling mount or a floor mount for your convenience.", '0.19: Garmin Approach R10 Launch Monitor: Try The Garmin Golf Membership For FreeTake virtual golfing for a test-drive with a free 30-day trial to the Garmin Golf app premium content3.E6 Connect CompatibilityThe E6 Connect library of content (not included) is compatible with Approach R10. With E6 Connect, easily play photorealistic courses whenever you want. Physical & PerformanceBattery type: internal rechargeable lithium-ionWater rating: IPX7Physical dimensions: 3.5" x 2.8" x 1" (88.5 x 70.25 x 25 mm) without tripodInterface: USBWeight:Without tripod: 5.22 oz (148 g) With tripod: 7.79 oz (220.8 g)Battery life: up to 10 hoursHigh-sensitivity receiver: No\xa0In the box:Approach R10Tripod standPhone mountCarry casemicroUSB cableDocumentation\xa01This device requires a paired compatible smartphone downloaded with the Garmin Golf app2Requires active subscription on the Garmin Golf app3In order to access your free trial, you must download the Garmin Golf app and provide your payment information.', "0.19: Skytrak+ Golf Simulator Studio Package: What's Included:  SkyTrak+ Launch Monitor  USB Cable USB Splitter Cable Quick Start Guide Product Information Guide SkyTrak App Virtual Driving Range    One Year of a SkyTrak Play & Improve Plan:   15 courses on WGT by TOPGOLF (IOS) 15 courses on TruGolf E6 Connect (IOS/PC)  Simulator Studio:   Studio Enclosure Optoma GT2000 HDR Projector Projector Mounting Arm 5x5 Hitting Mat Putting Turf Ball Tray Enclosure Side Netting Product Color or Size - (if number): 10' Product Price: 6995", '0.18: Optishot Golf In A Box 5 Golf Simulator: (H) is sufficient. Features:OPTISHOT2 SIMULATORThe OptiShot2 has swing and ball accuracy that is just like playing real golf. The OptiShot2 has precisely-tuned, high-speed infrared sensors giving you precise and instantaneous feedback on every shot.']context:['Can you tell me about the raspodo mobile launcher?', 'Can you recommend any products under 500 dollars? ']

As a chatbot for a golf e-commerce site, provide assistance based on the closed prompt. For queries that are about golf products not in the closed prompt or totally unrelated to the previous conversation, reply with: "This chatbot only answers questions about golf products in our database.", use the list called context to understand the past questions the user asked to help you answer future questions. User Query: Can you recommend any products under 500 dollars?
