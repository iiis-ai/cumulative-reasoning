# Examples excluded from FOLIO wiki curated

## Story ID: 226	Example ID: 640

- Hypothesis: William Dickinson did not get a seat in the Parliament.
- Label: True
- Premises:
  1. William Dickinson was a British politician who sat in the House of Commons
  2. William Dickinson attended Westminster school for high school and then the University of Edinburgh.
  3. The University of Edinburgh is a university located in the United Kingdom.
  4. William Dickinson supported the Portland Whigs.
  5. People who supported the Portland Whigs did not get a seat in the Parliament.
- Wrong Type: [Type 3: Inherent inconsistencies presented within the premises]

	We have a contradiction. On one hand, we have information that William Dickinson supported the Portland Whigs, and people who supported the Portland Whigs did not get a seat in the Parliament. On the other hand, another premise states that William Dickinson was a British politician who sat in the House of Commons, which implies that he did get a seat in the Parliament.

---
## Story ID: 226	Example ID: 641

- Hypothesis: William Dickinson went to schools located in the United Kingdom for both high school and university.
- Label: Unknown
- Premises:
  1. William Dickinson was a British politician who sat in the House of Commons
  2. William Dickinson attended Westminster school for high school and then the University of Edinburgh.
  3. The University of Edinburgh is a university located in the United Kingdom.
  4. William Dickinson supported the Portland Whigs.
  5. People who supported the Portland Whigs did not get a seat in the Parliament.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	We know that William Dickinson attended Westminster school for high school and the University of Edinburgh for university. There is a missing well-known common knowledge that Westminster school is located in the United Kingdom. Hence we cannot confirm that William Dickinson went to schools located in the United Kingdom for both high school and university.

---
## Story ID: 226	Example ID: 643

- Hypothesis: William Dickinson sat in the House of Commons.
- Label: True
- Premises:
  1. William Dickinson was a British politician who sat in the House of Commons
  2. William Dickinson attended Westminster school for high school and then the University of Edinburgh.
  3. The University of Edinburgh is a university located in the United Kingdom.
  4. William Dickinson supported the Portland Whigs.
  5. People who supported the Portland Whigs did not get a seat in the Parliament.
- Wrong Type: [Type 3: Inherent inconsistencies presented within the premises]

	We have a contradiction. On one hand, we have information that William Dickinson supported the Portland Whigs, and people who supported the Portland Whigs did not get a seat in the Parliament. On the other hand, another premise states that William Dickinson was a British politician who sat in the House of Commons, which implies that he did get a seat in the Parliament.

---
## Story ID: 82	Example ID: 252

- Hypothesis: Tom is a citizen of Washington.
- Label: Unknown
- Premises:
  1. Lawton Park is a neighbourhood in Seattle. 
  2. All citizens of Lawton Park use the zip code 98199. 
  3. Tom is a citizen of Lawton Park.
  4. Daniel uses the zip code 98199. 
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers] 

	We know that Tom is a citizen of Lawton Park, which is a neighborhood in Seattle. Although there is no direct information about the relationship between Seattle and Washington in the premises, It is common geographical fact that Seattle is a city in Washington state. Hence, it is reasonable to conclude that Tom is a citizen of Washington. However it is not certain only based on given premises.

---
## Story ID: 171	Example ID: 496

- Hypothesis: If you step on a stonefish and apply heat to the affected area, stings will cause death.
- Label: Unknown
- Premises:
  1. Some fish may sting.
  2. Stonefish is a fish.
  3. It stings to step on a stonefish.
  4. Stonefish stings cause death if not treated.
  5. To treat stonefish stings, apply heat to the affected area or use an antivenom.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers] 

  The premises state that applying heat to the affected area or using antivenom can treat stonefish stings. Thus, if heat is applied to the affected area, it should help treat the sting and prevent death. However, it is not certain that applying heat to the affected area will prevent death, as it is possible that the sting is too severe to be treated with heat.

---
## Story ID: 147	Example ID: 432

- Hypothesis: Inside Out was a punk band.
- Label: Unknown
- Premises:
  1. Vic DiCara plays guitar and bass.
  2. The only style of music Vic DiCara plays is punk music.
  3. Vic DiCara played in the band Inside Out.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	We know that Vic DiCara played in the band Inside Out and the only style of music he plays is punk music. This information implies that Inside Out played punk music while Vic DiCara was a member. However, it is not certain that Inside Out was a punk band, as it is possible that the band played a different style of music before Vic DiCara joined.

---
## Story ID: 236 Example ID: 673

- Hypothesis: Cancer researchers tend to use the cancer effect size to determine the relative importance of the genetic alterations that confer selective advantage to cancer cells.
- Label: Unknown
- Premises:
  1. Cancer biology is finding genetic alterations that confer selective advantage to cancer cells. 
  2. Cancer researchers have frequently ranked the importance of substitutions to cancer growth by P value.
  3. P values are thresholds for belief, not metrics of effect. 
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

  We can deduce that cancer researchers tend to use P values, not effect sizes, to rank the importance of genetic alterations. Thus, the hypothesis contradicts the premises. However, it is still possible that cancer researchers use the cancer effect size to determine the relative importance of the genetic alterations that confer selective advantage to cancer cells.

---
## Story ID: 56	Example ID: 167

- Hypothesis: Elizabeth is in a monarchy.
- Label: True
- Premises:
  1. If a person is the leader of a country for life, that person is in a monarchy. 
  2. Leaders are either a king or a queen.
  3. Queens are female.
  4. Kings are male. 
  5. Elizabeth is a queen.
  6. Elizabeth is a leader
- Wrong Type: [Type 1: Missing common knowledge or contradictory to common knowledge in the premises]

	We know that Elizabeth is a queen and a leader of a country. However, it is not explicitly stated whether Elizabeth is the leader of a country for life. Thus, we cannot confirm if Elizabeth is in a monarchy. In fact, it is well known that Elizabeth is the queen of the United Kingdom, which is a constitutional monarchy.

---
## Story ID: 73	Example ID: 223

- Hypothesis: There is a species of Ambiortus that doesn't live in the Mongol region.
- Label: False
- Premises:
  1. Ambiortus is a prehistoric bird genus.
  2. Ambiorus Dementjevi is the only known species of Ambiortus.
  3. The Mongol region was where Ambiorus Dementjevi lived.
  4. Yevgeny Kurochkin was the discoverer of Ambiortus.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers] 

  We learn that there is only one known species of Ambiortus, which is Ambiorus Dementjevi. The Mongol region is where Ambiorus Dementjevi lived. However, we do not know if there are other unknown species of Ambiortus that live in other regions.


---
## Story ID: 3	Example ID: 9

- Hypothesis: Fort Carillon was located in Europe.
- Label: Unknown
- Premises:
  1. Fort Ticonderoga is the current name for Fort Carillon.
  2. Pierre de Rigaud de Vaudreuil built Fort Carillon.
  3. Fort Carillon was located in New France.
  4. New France is not in Europe.
- Wrong Type: [Type 5: Incorrect answers]

	We know that Fort Carillon was located in New France, and New France is not in Europe. Therefore, Fort Carillon was not located in Europe.

---
## Story ID: 222	Example ID: 632

- Hypothesis: Some people flying from New York City to Seattle will be uncomfortable.
- Label: False
- Premises:
  1. New York City is on the East Coast. 
  2. Seattle is on the West Coast. 
  3. If a person from a city on the East coast is traveling to a city on the west coast, they will be on a long flight.
  4. Most passengers on flights to Seattle from New York City are not in first class.
  5. People on long flights are uncomfortable unless they're in first class
- Wrong Type: [Type 5: Incorrect answers]

  We can deduce the following:

  1. A person traveling from New York City to Seattle will be on a long flight (since New York City is on the East Coast and Seattle is on the West Coast).
  2. Most passengers on flights from New York City to Seattle are not in first class.
  3. People on long flights are uncomfortable unless they're in first class.

  Given this information, we can conclude that some people flying from New York City to Seattle will be uncomfortable, as most of them are not in first class and long flights cause discomfort for those not in first class.

---
## Story ID: 47	Example ID: 136

- Hypothesis: The Controlled Substances Act prevents harmful things.
- Label: Unknown
- Premises:
  1. A controlled substance is a drug.
  2. There exist both harmful and beneficial controlled substances.
  3. If a child is exposed to a controlled substance, he or she is in chemical endangerment.
  4. Chemical Endangerment is harmful. 
  5. The Controlled Substances Act was an act passed in 1971.
  6. Some Acts prevent harmful things.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	We know that the Controlled Substances Act is related to controlled substances and chemical endangerment, which is harmful. The premises also mention that there exist both harmful and beneficial controlled substances. While the Controlled Substances Act may prevent harmful things, it may also prevent some beneficial things. Thus, it is not entirely accurate to say that the Controlled Substances Act prevents harmful things exclusively, as it may also have an impact on beneficial things.

---
## Story ID: 200	Example ID: 573

- Hypothesis: If someone is cooking downstairs, it will always cause the first floor to become smokey.
- Label: Unknown
- Premises:
  1. There are two kitchens in the house: the upstairs kitchen and the downstairs kitchen.
  2. When someone is cooking in the downstairs kitchen, the first floor becomes smokey unless the air conditioner is running.
  3. If the air conditioner is running and someone is cooking in the downstairs kitchen, all the smoke travels to the second floor.
- Wrong Type: [Type 5: Incorrect answers]

	We can conclude the following:

  1. If the air conditioner is running and someone is cooking in the downstairs kitchen, all the smoke travels to the second floor.
  2. When someone is cooking in the downstairs kitchen, the first floor becomes smokey unless the air conditioner is running.

  These premises imply that it's not always the case that the first floor becomes smokey when someone is cooking downstairs because it depends on whether or not the air conditioner is running.

---
## Story ID: 146	Example ID: 431

- Hypothesis: Callus 4 is written in an unusual iambic trimeter to convey a strong analogy of human aging.
- Label: False
- Premises:
  1. Callus 4 is a poem that was written by the ancient Roman writer Catullus.
  2. Callus 4 is a story about the retirement of a well-traveled ship.
  3. There is a strong analogy of human aging in the poem Callus 4.
  4. Callus 4 is written in an unusual iambic trimeter to convey a sense of speed over the waves.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	We understand that Callus 4 is a poem written by Catullus, and it contains a strong analogy of human aging. We also know that the poem is written in an unusual iambic trimeter, but it is mentioned that this is used to convey a sense of speed over the waves, not to convey the strong analogy of human aging. However, it is not explicitly stated that the unusual iambic trimeter is not used to convey the strong analogy of human aging.

---
## Story ID: 235	Example ID: 671

- Hypothesis: Michael Crichton has directed a film about robots.
- Label: Unknown
- Premises:
  1. Westworld is an American science fiction-thriller TV series.
  2. In 2016, a new television series named Westworld debuted on HBO.
  3. The TV series Westworld is adapted from the original film in 1973, which was written and directed by Michael Crichton.
  4. The 1973 film Westworld is about robots that malfunction and begin killing the human visitors.
- Wrong Type: [Type 5: Incorrect answers]

	We can deduce that Michael Crichton wrote and directed the 1973 film Westworld, which is about robots that malfunction and begin killing the human visitors. Thus, it is true that Michael Crichton has directed a film about robots.

---
## Story ID: 231	Example ID: 660

- Hypothesis: The United States won fewer gold medals than China.
- Label: Unknown
- Premises:
  1. The 2008 Summer Olympics were held in Beijing, China.
  2. The 2008 Summer Olympics were the second Summer Olympic Games to be held in a communist state.
  3. China won the most gold medals (48) in the 2008 Summer Olympics.
  4. The United States placed second in the gold medal tally but won the highest number of medals overall (112) in the 2008 Summer Olympics.
  5. The third place in the gold medal tally was achieved by Russia in the 2008 Summer Olympics.
  6. If a country places third in gold medals, then they had fewer gold medals than the team that won the most gold medals.
  7. 87 countries won at least one medal during the 2008 Games.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	We know that China won 48 gold medals and placed first in the gold medal tally during the 2008 Summer Olympics. The United States placed second in the gold medal tally. Since the United States placed second, it indicates that they won fewer gold medals than China, who placed first. However, the conclusion does not specify which year the United States won fewer gold medals than China. It is possible that the United States won fewer gold medals than China in the 2008 Summer Olympics, but it is also possible that the United States won fewer gold medals than China in a different year.

---
## Story ID: 29	Example ID: 84

- Hypothesis: Gasteren is a Dutch village.
- Label: Unknown
- Premises:
  1. Gasteren is village located in the province of Drenthe.
  2. Drenthe is a Dutch province. 
  3. No cities are villages.
  4. The population of a village in Drenthe was 155 people.
- Wrong Type: [Type 5: Incorrect answers]

	We know that Gasteren is a village located in Drenthe, and Drenthe is a Dutch province. Since Gasteren is within a Dutch province, it can be concluded that Gasteren is a Dutch village.


---
## Story ID: 210	Example ID: 605

- Hypothesis: Platypuses are vertebrates.
- Label: Unknown
- Premises:
  1. The only types of mammals that lay eggs are platypuses and echidnas.
  2. Platypuses are not hyrax.
  3. Echidnas are not hyrax.
  4. No mammals are invertebrates.
  5. All animals are either vertebrates or invertebrates.
  6. Mammals are animals.
  7. Hyraxes are mammals.
  8. Grebes lay eggs.
  9. Grebes are not platypuses and also not echidnas.
- Wrong Type: [Type 5: Incorrect answers]

	We can deduce the following:

1. Platypuses are mammals (since they are one of the only types of mammals that lay eggs).
2. Mammals are animals.
3. No mammals are invertebrates.
4. All animals are either vertebrates or invertebrates.

Since platypuses are mammals, and no mammals are invertebrates, platypuses cannot be invertebrates. Therefore, platypuses must be vertebrates, as all animals are either vertebrates or invertebrates.

---
## Story ID: 89	Example ID: 273

- Hypothesis: Bobby Flynn was born in Queens.
- Label: Unknown
- Premises:
  1. Bobby Flynn is a singer-songwriter. 
  2. Bobby Flynn finished 7th while competing on Australian Idol.
  3. Australian Idol competitors are Australian citizens.
  4. The Omega Three band made a nationwide tour in 2007.
  5. Bobby Flynn is a member of The Omega Three band.
  6. Bobby Flynn was born in Queensland.
- Wrong Type: [Type 5: Incorrect answers]

	We know that Bobby Flynn was born in Queensland, which is a state in Australia. Queens is a borough in New York City, and there is no information in the premises that suggests Bobby Flynn was born in Queens.

---
## Story ID: 98	Example ID: 298

- Hypothesis: Maggie Friedman developed Witches of East End.
- Label: Unknown
- Premises:
  1. One American screenwriter and producer is Maggie Friedman.
  2. Maggie Friedman was the showrunner and executive producer of the lifetime television series Witches of East End.
  3. Witches of East End is a fantasy-drama series.
  4. Maggie Friedman produced and developed Eastwick.
  5. Eastwick is a series by ABC.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	We can deduce that Maggie Friedman was the showrunner and executive producer of the lifetime television series Witches of East End. Generally, the role of a showrunner and executive producer includes developing the series. Therefore, it is reasonable to conclude that Maggie Friedman developed Witches of East End. However, it is not certain that Maggie Friedman developed Witches of East End, as it is possible that she only produced the series.

---
## Story ID: 249	Example ID: 698

- Hypothesis: Luke is a chef.
- Label: False
- Premises:
  1. Every chef can cook.
  2. Some people who aren’t chefs can cook.
  3. People who cook can make scrambled eggs and pasta.
  4. If someone can make cookies and muffins, they are a baker.
  5. Bakers who can also make scrambled eggs can make a good breakfast.
  6. Luke can make cookies, scrambled eggs, and muffins, but not pasta.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

The premises state that Peopole who cook can make scrambled eggs and pasta, Luke can make cookies, scrambled eggs, and muffins, but not pasta. Thus, we can conclude that Luke is not a chef. However, this deduction is heavily based on the premise: ''People who cook can make scrambled eggs and pasta.'' This premise is not a common knowledge and not convincing, and it is possible that people who cook can make scrambled eggs but not pasta. Therefore, we cannot confirm that Luke is not a chef.

---
## Story ID: 196	Example ID: 563

- Hypothesis: ETS administers international tests including the TOEFL, GRE and subject tests in China.
- Label: Unknown
- Premises:
  1. ETS develops various standardized tests primarily in the United States for K-12 and higher education. 
  2. ETS administers international tests including the TOEFL, TOEIC, GRE and subject tests in more than 180 countries.
  3. Many of the assessments ETS develops are associated with entry to the US tertiary and quaternary education institutions. 
  4. ETS also develops K-12 statewide assessments used for accountability testing in many states.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	We know that ETS administers international tests, including TOEFL, GRE, and subject tests, in more than 180 countries. China is not mentioned explicitly, but it is reasonable to assume that China is one of those 180 countries.

---
## Story ID: 134	Example ID: 396

- Hypothesis: Sally's company utilizes the installment sales method.
- Label: True
- Premises:
  1. The installment sales method is the approach to recognize revenue under the US GAAP.
  2. In accrual accounting, revenues are recognized when they are realized.
  3. In cash accounting, revenues are recognized when cash is received.
  4. The US GAAP is the accounting standard developed and used by the US Securities and Exchange Commission.
  5. Sally works for the US Securities and Exchange Commission.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	We can infer that Sally works for the US Securities and Exchange Commission, which uses the US GAAP accounting standard. The installment sales method is mentioned as an approach to recognize revenue under the US GAAP. However, there is no direct information about Sally's company utilizing the installment sales method.

---
## Story ID: 12	Example ID: 34

- Hypothesis: Water from the Croton River flows to the Bronx.
- Label: Unknown
- Premises:
  1. The Croton River watershed is the drainage basin of the Croton River.
  2. The Croton River is in southwestern New York.
  3. Water from the Croton River watershed flows to the Bronx.
  4. The Bronx is in New York.
- Wrong Type: [Type 1: Missing common knowledge or contradictory to common knowledge in the premises]

	We understand that the Croton River is in southwestern New York, and the Bronx is also located in New York. It is stated that water from the Croton River watershed flows to the Bronx, and the Croton River watershed is the drainage basin of the Croton River. It is common knowledge that water from a river flows to its drainage basin. Therefore, it is true that water from the Croton River flows to the Bronx.

---
## Story ID: 238	Example ID: 682

- Hypothesis: Daniel studied bioengineering as his major at Rice University.
- Label: True
- Premises:
  1. Daniel is a software engineer and he works at Palantir Technologies.
  2. Daniel studied bioengineering during his undergraduate at Rice University.
  3. Daniel’s older sister works at Meta as a technical sourcer. 
  4. Daniel’s dad and older sister both graduated from Stanford University.
  5. Daniel’s dad is a doctor practicing internal medicine at a veteran’s hospital in Minneapolis
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	It is clearly stated that Daniel studied bioengineering during his undergraduate at Rice University. However, there is no direct information about Daniel's major at Rice University. It is possible that Daniel studied bioengineering as his major at Rice University, but it is also possible that he studied a different major.

---
## Story ID: 108	Example ID: 330

- Hypothesis: There is a commercial plane made by both Airbus and Boeing.
- Label: False
- Premises:
  1. All commerical aircraft are produced by either Boeing or Airbus.
  2. All American Airlines jets are commerical aircraft. 
  3. Airbus made more in revenue than Boeing last year.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	We can deduce that all commercial aircraft are produced by either Boeing or Airbus. However, there is no information about a commercial plane made by both Airbus and Boeing together.

---
## Story ID: 229	Example ID: 654

- Hypothesis: Barbara Ann Marshall did not receive medals.
- Label: Unknown
- Premises:
  1. Barbara Ann Marshall is a former swimmer and former world record-holder.
  2. Barbara Ann Marshall participated in the 1972 Summer Olympics.
  3. Barbara Ann Marshall's home country is the United States.
  4. All people who compete in the 1972 Summer Olympics represent their home country.
  5. Barbara Ann Marshall participated in the preliminary heat in the freestyle relay.
  6. Barbara Ann Marshall did not participate in the event final of the 1972 Summer Olympics freestyle relay.
  7. Only relay swimmers who participated in the event final received medals.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	We gather that Barbara Ann Marshall:

1. Participated in the 1972 Summer Olympics.
2. Participated in the preliminary heat in the freestyle relay.
3. Did not participate in the event final of the 1972 Summer Olympics freestyle relay.

Additionally, the premises state that only relay swimmers who participated in the event final received medals. Since Barbara Ann Marshall did not participate in the event final, it can be concluded that she did not receive medals in the 1972 Summer Olympics. However, there is no direct information about whether or not Barbara Ann Marshall received medals in other events.

---
## Story ID: 201	Example ID: 578

- Hypothesis: It is possible to complete the game without ever reaching the green stage.
- Label: Unknown
- Premises:
  1. A game is played with three stages: red stage, yellow stage, and green stage.
  2. Each player begins at the red stage.
  3. All players must reach the yellow stage before they can reach the green stage.
  4. The yellow stage comes after the red stage.
  5. All players must proceed one stage at a time.
- Wrong Type: [Type 5: Incorrect answers]

	We understand that:

1. Each player begins at the red stage.
2. The yellow stage comes after the red stage.
3. All players must reach the yellow stage before they can reach the green stage.
4. All players must proceed one stage at a time.

Considering this information, it is clear that every player must complete the red stage, then proceed to the yellow stage, and finally reach the green stage. Therefore, it is not possible to complete the game without ever reaching the green stage.

---
## Story ID: 181	Example ID: 526

- Hypothesis: Captain America speaks Spanish.
- Label: Unknown
- Premises:
  1. An American superhero comes from either DC universe or Marvel universe.
  2. Captain America is a superhero.
  3. Captain America is an American.
  4. Captain America does not come from DC universe.
  5. If a superhero is American, he speaks English.
  6. A superhero speaks English or Spanish.
- Wrong Type: [Type 1: Missing common knowledge or contradictory to common knowledge in the premises]

	We know that Captain America is an American superhero and speaks English, as stated in the second proposition. However, there is no direct information about Captain America speaking Spanish. While someone may be mistaken to think that Captain America speaks English so that he must not speak Spanish, It is common knowledge that someone can speak more than one language.

---
## Story ID: 149	Example ID: 437

- Hypothesis: Judd Bankert competed in the 1992 Winter Olympics.
- Label: True
- Premises:
  1. Guam has participated in the Winter Olympics.
  2. In 1988, the Winter Olympics were held in Calgary.
  3. Guam sent an athlete to the Calgary Winter Olympics.
  4. If Guan sent an athlete to the Calgary Winter Olympics, then it participated in the Calgary Winter Olympics.
  5. Judd Bankert is the only athlete from Guam who has ever competed in the Winter Olympics.
- Wrong Type: [Type 5: Incorrect answers]

	We learn the following information:

- Guam sent an athlete to the Calgary Winter Olympics.
- Judd Bankert is the only athlete from Guam who has ever competed in the Winter Olympics.
- Guam has participated in the Winter Olympics.
- In 1988, the Winter Olympics were held in Calgary.

However, we have no information about when Judd Bankert competed in the Winter Olympics, only that he is the only athlete from Guam who has ever competed in them. We know that he participated in the Calgary Winter Olympics in 1988, but we cannot determine whether or not he competed in the 1992 Winter Olympics based on the given information.

---
## Story ID: 54	Example ID: 162

- Hypothesis: Roundels can be deployed on roundels.
- Label: True
- Premises:
  1. A roundel is a rounded artillery fortification.
  2. A roundel is not higher than adjacent walls. 
  3. Cannons can be deployed on artillery fortifications. 
  4. Roundels are the oldest artillery fortifications.
  5. Battery towers are an artillery fortification.
- Wrong Type: [Type 1: Missing common knowledge or contradictory to common knowledge in the premises]

	We know that roundels are artillery fortifications and cannons can be deployed on artillery fortifications. However, the information provided does not directly address whether roundels can be deployed on other roundels. It is common knowledge that cannons can be deployed on other cannons. Therefore, it is reasonable to conclude that roundels can be deployed on roundels.

---
## Story ID: 158	Example ID: 456

- Hypothesis: They have at leat one candidate city in Florida to visit.
- Label: Unknown
- Premises:
  1. Mr. and Mrs. Smith make a travel plan, they want to go to a city in California or Florida, and where neither of them has ever been.
  2. Cities in California that they are interested in are San Francisco, Los Angeles, and San Diego.
  3. Cities in Florida that they are interested in are Orlando and Miami.
  4. Mr. Smith has been to two cities in California.
  5. Mrs. Smith has been to one city in Florida.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	We know that Mr. and Mrs. Smith are interested in visiting certain cities in California and Florida where neither of them has been before. However, the premises don't provide enough information about which cities they have visited. Mrs. Smith has been to one city in Florida, but we don't know if it's Orlando or Miami. Therefore, we cannot confirm if they have at least one candidate city in Florida to visit.

---
## Story ID: 158	Example ID: 457

- Hypothesis: They have at least two candidate cities in California to visit.
- Label: Unknown
- Premises:
  1. Mr. and Mrs. Smith make a travel plan, they want to go to a city in California or Florida, and where neither of them has ever been.
  2. Cities in California that they are interested in are San Francisco, Los Angeles, and San Diego.
  3. Cities in Florida that they are interested in are Orlando and Miami.
  4. Mr. Smith has been to two cities in California.
  5. Mrs. Smith has been to one city in Florida.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	We know that Mr. and Mrs. Smith are interested in visiting cities in California and Florida where neither of them has been before. Mr. Smith has been to two cities in California, but we don't know which ones. There are three cities in California they are interested in: San Francisco, Los Angeles, and San Diego. Since Mr. Smith has visited two of them, there must be at least one city in California they can visit together. However, we cannot conclude that they have at least two candidate cities in California to visit, as Mr. Smith may have already visited two of the three cities they are interested in.

---
## Story ID: 88	Example ID: 268

- Hypothesis: Bernarda Bryson Shahn was born in Greece.
- Label: Unknown
- Premises:
  1. Bernarda Bryson Shahn was a painter and lithographer.
  2. Bernarda Bryson Shahn was born in Athens, Ohio. 
  3. Bernarda Bryson Shahn was married to Ben Shahn.
  4. People born in Athens, Ohio are Americans.
- Wrong Type: [Type 1: Missing common knowledge or contradictory to common knowledge in the premises]

	We know that Bernarda Bryson Shahn was born in Athens, Ohio. It is common knowledge that Greece is not in Ohio. It also states that people born in Athens, Ohio, are Americans. Thus, it is false to conclude that Bernarda Bryson Shahn was born in Greece. 

---
## Story ID: 161	Example ID: 464

- Hypothesis: Zhang's English score is lower than 95.
- Label: True
- Premises:
  1. There are five grades including A+, A, B+, B, and C in English.
  2. If a student gets A+ in English, then his score is greater than 95.
  3. If a student gets A in English, then his score is in the range of 90-95.
  4. Zhang got an A in English.
  5. Wang's English score is better than Zhang's.
  6. Wu's English score is lower than 90.
- Wrong Type: [Type 5: Incorrect answers]

	We know that Zhang got an A in English, which means his score is in the range of 90-95. Therefore, Zhang's English score is not lower than 95. As 9s is in the range of 90-95. The correct conclusion should be Zhang's English score is equals to 95 or lower than 95.

---
## Story ID: 18	Example ID: 52

- Hypothesis: Miroslav Fiedler was a French mathematician.
- Label: Unknown
- Premises:
  1. Miroslav Fiedler was a Czech mathematician.
  2. Miroslav Fiedler is known for his contributions to linear algebra and graph theory.
  3. Miroslav Fiedler is honored by the Fiedler eigenvalue.
  4. Fiedler eigenvalue is the second smallest eigenvalue of the graph Laplacian.
- Wrong Type: [Type 5: Incorrect answers]

	We know that Miroslav Fiedler was a Czech mathematician. This contradicts the hypothesis, which states that Miroslav Fiedler was a French mathematician. It is common knowledge that if someone is a Czech mathematician, he is not a French mathematician. Therefore, it is false that Miroslav Fiedler was a French mathematician.

---
## Story ID: 48	Example ID: 141

- Hypothesis: The Salmon of Doubt has no innovative Ideas.
- Label: Unknown
- Premises:
  1. Douglas Adams is an author who created the book collection called The Salmon of Doubt. 
  2. The Salmon of Doubt is about life experiences and technology.
  3. All authors are writers.
  4. Writers create innovative ideas.
  5. Some books that contain innovative ideas are about technology.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	We know that Douglas Adams is an author who created the book collection called The Salmon of Doubt, which is about life experiences and technology. All authors are writers, and writers create innovative ideas. Some books that contain innovative ideas are about technology. Based on this information, it is highly likely that The Salmon of Doubt contains innovative ideas.

---
## Story ID: 32	Example ID: 95

- Hypothesis: Hugh Vanstone attended school in the US.
- Label: Unknown
- Premises:
  1. Hugh Vanstone is one of the world's leading lighting designers. 
  2. Hugh Vanstone is from the UK.
  3. Hugh Vanstone has lit more than 160 productions.
  4. Hugh Vanstone attended school where he is from. 
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	We know that Hugh Vanstone is from the UK and attended school in the UK. There is no information provided about Hugh Vanstone attending school in the US.

---
## Story ID: 106	Example ID: 322

- Hypothesis: Ralph Hammerthaler is a writer born in Asia.
- Label: Unknown
- Premises:
  1. Ralph Hammerthaler was born in Wasserburg am Inn.
  2. Wasserburg am Inn is in Germany.
  3. Germany is in Europe.
  4. Ralph Hammerthaler is a German writer.
  5. Ralph Hammerthaler was born in 1965. 
- Wrong Type: [Type 5: Incorrect answers]

	We know that Ralph Hammerthaler was born in Wasserburg am Inn, which is in Germany. Germany is located in Europe, not Asia. It is common knowledge that a country cannot be in both Europe and Asia. Therefore, it is false that Ralph Hammerthaler is a writer born in Asia.

---
## Story ID: 21	Example ID: 62

- Hypothesis: The Golden State Warriors will have more income for gate receipts.
- Label: True
- Premises:
  1. The Golden State Warriors are a team from San Francisco.
  2. The Golden State Warriors won the NBA finals.
  3. All teams attending the NBA finals have more than thirty years of history.
  4. Boston Celtics are a team that lost the NBA finals.
  5. If a team wins the NBA finals, then they will have more income.
  6. If a team wins or loses at the NBA finals, then they are attending the finals.
- Wrong Type: [Type 1: Missing common knowledge or contradictory to common knowledge in the premises]

	We know that the Golden State Warriors won the NBA finals and that if a team wins the NBA finals, they will have more income. Therefore, we can infer that the Golden State Warriors will have more income. However, the hypothesis mentions 'more income for gate receipts,' and there is no information about gate receipts in the premises.

---
## Story ID: 218	Example ID: 624

- Hypothesis: Maya will not play violin.
- Label: True
- Premises:
  1. Maya will play violin if and only if she never injures her fingers.
  2. Volleyball players can injure their ankle, fingers, or shoulder.
  3. Maya is a volleyball player.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	We know that Maya is a volleyball player and she will play violin if and only if she never injures her fingers. It is also mentioned that volleyball players can injure their ankle, fingers, or shoulder. However, we do not have any specific information about whether Maya has injured her fingers or not.

---
## Story ID: 266	Example ID: 715

- Hypothesis: Some CD players are suitable toys for children.
- Label: Unknown
- Premises:
  1. All CD players are delicate mechanisms.
  2. No delicate mechanisms are suitable toys for children.
- Wrong Type: [Type 5: Incorrect answers]

	We can deduce the following:

1. All CD players are delicate mechanisms.
2. No delicate mechanisms are suitable toys for children.

Since all CD players are delicate mechanisms and no delicate mechanisms are suitable toys for children, it follows that no CD players are suitable toys for children.

---
## Story ID: 39	Example ID: 116

- Hypothesis: White Town was a successful band.
- Label: Unknown
- Premises:
  1. "Your Woman" is a song by British one-man band White Town.
  2. "Your Woman" song peaked at No. 1 on the UK Singles Chart.
  3. If a song peaked at No.1 at a cetain place, then it was extremely popular.
  4. "Your Woman" also peaked No. 1 in Iceland, Israel and Spain.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	We learn that "Your Woman," a song by White Town, was extremely popular and peaked at No. 1 in multiple countries. However, the success of a single song does not necessarily guarantee the overall success of the band. The hypothesis claims that White Town was a successful band, but the premises only provide information about the success of one specific song.

---
## Story ID: 13	Example ID: 36

- Hypothesis: System 7 has released several singles.
- Label: Unknown
- Premises:
  1. System 7 is a UK-based electronic dance music band.
  2. Steve Hillage and Miquette Giraudy formed System 7.
  3. Steve Hillage and Miquette Giraudy are former members of the band Gong.
  4. Electric dance music bands are bands.
  5. System 7 has released several club singles.
  6. Club singles are not singles.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	We know that System 7 is an electronic dance music band formed by Steve Hillage and Miquette Giraudy. It is also stated that System 7 has released several club singles. However, the premises also state that club singles are not singles. Based on this information, we cannot conclude that System 7 has released several singles.

---
## Story ID: 220	Example ID: 629

- Hypothesis: The single "1901" is a certified gold single.
- Label: Unknown
- Premises:
  1. The indie pop band Phoenix has released 6 albums. 
  2. Phoenix's album "Wolfgang Amadeus Phoenix" sold over 500,000 copies. 
  3. A certified gold album or single is one which sold over half a million copies. 
  4. "1901" is a single from Phoenix's album "Wolfgang Amadeus Phoenix."
  5. Over 400,000 copies of "1901" have been sold. 
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	We know that "1901" is a single from Phoenix's album "Wolfgang Amadeus Phoenix" and that over 400,000 copies of "1901" have been sold. However, we also know that a certified gold album or single is one that sold over half a million copies (500,000). Since "1901" didn't reach the 500,000 copies sold mark, it is not a certified gold single.

---
## Story ID: 85	Example ID: 261

- Hypothesis: Diethylcarbamazine is used in the treatment of filariasis.
- Label: Unknown
- Premises:
  1. Diethylcarbamazine is a medication discovered in the year 1947.
  2. Diethylcarbamazine can be used to treat river blindness.
  3. The only preferred treatment for river blindness is ivermectin.
  4. Diethylcarbamazine is not ivermectin.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	We know that diethylcarbamazine is a medication that is not ivermectin, and it can be used to treat river blindness. River blindness is a form of filariasis. Therefore, it can be concluded that diethylcarbamazine is used in the treatment of filariasis. Hovever, there are other forms of filariasis, and we do not know if diethylcarbamazine is used in the treatment of those forms.

---
## Story ID: 114	Example ID: 345

- Hypothesis: No cutmen appear in boxing matches.
- Label: Unknown
- Premises:
  1. A cutman is responsible for preventing and treating physical damage to a fighter.
  2. Cutmen appear in matches such as a boxing, kickboxing or a mixed martial arts bout. 
  3. Cutmen typically handle swelling, nosebleeds and lacerations. 
  4. Jack is a cutman.
- Wrong Type: [Type 5: Incorrect answers]

	We learn that cutmen handle physical damage to fighters and appear in matches such as boxing, kickboxing, or mixed martial arts bouts. This directly contradicts the hypothesis that no cutmen appear in boxing matches.

---
## Story ID: 301	Example ID: 750

- Hypothesis: V is invigorating
- Label: Unknown
- Premises:
  1. When something is depressing, it is sad.
  2. V is depressing. 
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	We learn that V is depressing and when something is depressing, it is sad. However, there's no information provided about whether V is invigorating or not.

---
## Story ID: 103	Example ID: 314

- Hypothesis: John Evans Popularized the term paalstab.
- Label: Unknown
- Premises:
  1. Palstaves are a type of early bronze axe.
  2. Commonly found in northern, western and south-western Europe, palstaves are cast in moulds.
  3. John Evans is an archeologist who popularized the term "palstave".
  4. A paalstab is not an axe, but rather a digging shovel.
- Wrong Type: [Type 4: Vague premises or typographical errors]

  What is palstave and paalstab? Were they misspelled?

	We know that John Evans popularized the term 'palstave,' which is a type of early bronze axe. However, the hypothesis is about 'paalstab,' which is a digging shovel and not the same term as 'palstave.' There is no information provided about John Evans popularizing the term 'paalstab.'

---
## Story ID: 103	Example ID: 315

- Hypothesis: There is an axe that is commonly found in Western Europe.
- Label: Unknown
- Premises:
  1. Palstaves are a type of early bronze axe.
  2. Commonly found in northern, western and south-western Europe, palstaves are cast in moulds.
  3. John Evans is an archeologist who popularized the term "palstave".
  4. A paalstab is not an axe, but rather a digging shovel.
- Wrong Type: [Type 4: Vague premises or typographical errors]

	We can see that palstaves are a type of early bronze axe and they are commonly found in northern, western, and south-western Europe. Therefore, it is true that there is an axe that is commonly found in Western Europe. However, the premises also state that a paalstab is not an axe, but rather a digging shovel.

---
## Story ID: 90	Example ID: 276

- Hypothesis: Koei Tecmo holds anime.
- Label: Unknown
- Premises:
  1. Koei Tecmo is a Japanese video game and anime holding company.
  2. Holding companies hold several companies.
  3. Tecmo was disbanded in Japan, while Koei survived, but was renamed.
  4. Video game holding companies are holding companies.
- Wrong Type: [Type 5: Incorrect answers]

	We know that Koei Tecmo is a Japanese video game and anime holding company. Since holding companies hold several companies, and Koei Tecmo is specifically stated to be an anime holding company, it can be concluded that Koei Tecmo holds anime companies.

---
## Story ID: 199	Example ID: 572

- Hypothesis: The Playstation Camera can be used for all Playstation consoles.
- Label: Unknown
- Premises:
  1. The PlayStation EyeToy is a camera accessory for the Playstation 2. 
  2. The PlayStation Eye is a camera accessory for the Playstation 3.
  3. The Playstation Camera is a camera accessory for the Playstation 4 and the Playstation 5.
  4. Camera accessory for the system is compatible with that system
  5. Only the Playstation Camera is compatible with more than one system.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	We learn that:

1. The PlayStation Eye is compatible with the PlayStation 3.
2. The PlayStation EyeToy is compatible with the PlayStation 2.
3. The PlayStation Camera is compatible with the PlayStation 4 and the PlayStation 5.

The hypothesis states that the PlayStation Camera can be used for all PlayStation consoles. However, the information provided indicates that different camera accessories are compatible with different PlayStation consoles, but not all of them. The PlayStation Camera is only compatible with the PlayStation 4 and the PlayStation 5, not the PlayStation 2 or PlayStation 3.

---
## Story ID: 99	Example ID: 299

- Hypothesis: Baku is southeast of Shafaq-Asiman.
- Label: Unknown
- Premises:
  1. Shafaq-Asiman is a large complex of offshore geological structures in the Caspian Sea.
  2. Baku is northwest of Shafaq-Asiman.
  3. If place A is northwest of place B, then place B is southeast of place A.
- Wrong Type: [Type 5: Incorrect answers]

	We know that Baku is northwest of Shafaq-Asiman, and if place A is northwest of place B, then place B is southeast of place A. Since Baku (place A) is northwest of Shafaq-Asiman (place B), it is true that Shafaq-Asiman is southeast of Baku.

---
## Story ID: 71	Example ID: 215

- Hypothesis: Herodicus was tutored by Hippocrates.
- Label: Unknown
- Premises:
  1. Herodicus was a Greek physician, dietician, sophist, and gymnastic-master.
  2. Herodicus was born in the city of Selymbria.
  3. Selymbria is a colony of the city-state Megara.
  4. One of the tutors of Hippocrates was Herodicus.
  5. Massages were recommended by Herodicus.
  6. Some of theories of Herodicus are considered to be the foundation of sports medicine.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	We learn that Herodicus tutored Hippocrates. Therefore, the hypothesis that Herodicus was tutored by Hippocrates is contrary to the information given.

---
## Story ID: 71	Example ID: 216

- Hypothesis: Herodicus was born in a city-state.
- Label: Unknown
- Premises:
  1. Herodicus was a Greek physician, dietician, sophist, and gymnastic-master.
  2. Herodicus was born in the city of Selymbria.
  3. Selymbria is a colony of the city-state Megara.
  4. One of the tutors of Hippocrates was Herodicus.
  5. Massages were recommended by Herodicus.
  6. Some of theories of Herodicus are considered to be the foundation of sports medicine.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	We know that Herodicus was born in the city of Selymbria, which is a colony of the city-state Megara. A colony is typically established and governed by a city-state. Therefore, it is reasonable to conclude that Herodicus was born in a city-state.

---
## Story ID: 74	Example ID: 228

- Hypothesis: Camp Davern was established in 1989.
- Label: Unknown
- Premises:
  1. Camp Davern is a traditional summer camp for boys and girls.
  2. Camp Davern was established in the year 1946.
  3. Camp Davern was operated by the YMCA until the year 2015.
  4. Camp Davern is one of Ontario's oldest summer camps.
- Wrong Type: [Type 1: Missing common knowledge or contradictory to common knowledge in the premises]

	We can clearly see that Camp Davern was established in the year 1946 and not 1989. It is common knowledge that an organization cannot be established in two different years.

---
## Story ID: 157	Example ID: 452

- Hypothesis: Blueberries were the most popular fruit at the party.
- Label: Unknown
- Premises:
  1. The party provides five kinds of fruits: strawberry, orange, blueberry, grape, and cherry.
  2. All fruits are provided in the same weight at the beginning of the party.
  3. If the fruit had the lowest remaining weight at the end of the party, then it means it was the most popular fruit.
  4. At the end of the party, strawberries had the lowest remaining weight.
  5. At the end of the party, the amount of leftover blueberries was lower than that of cherries.
  6. Benjamin only ate oranges and grapes at the party.
- Wrong Type: [Type 5: Incorrect answers]

	we know that there were five kinds of fruits provided at the party, and strawberries had the lowest remaining weight at the end. It is also mentioned that if a fruit had the lowest remaining weight, it means it was the most popular fruit.

Since strawberries had the lowest remaining weight, they were the most popular fruit at the party. This contradicts the hypothesis that blueberries were the most popular fruit.

---
## Story ID: 157	Example ID: 453

- Hypothesis: Cherries were the most popular fruit at the party.
- Label: Unknown
- Premises:
  1. The party provides five kinds of fruits: strawberry, orange, blueberry, grape, and cherry.
  2. All fruits are provided in the same weight at the beginning of the party.
  3. If the fruit had the lowest remaining weight at the end of the party, then it means it was the most popular fruit.
  4. At the end of the party, strawberries had the lowest remaining weight.
  5. At the end of the party, the amount of leftover blueberries was lower than that of cherries.
  6. Benjamin only ate oranges and grapes at the party.
- Wrong Type: [Type 5: Incorrect answers]

	we can infer that strawberries had the lowest remaining weight at the end of the party. Additionally, the premises state that if a fruit had the lowest remaining weight at the end of the party, it means it was the most popular fruit. Therefore, it can be deduced that strawberries were the most popular fruit at the party.

---
## Story ID: 122	Example ID: 367

- Hypothesis: A shetani is either mythological or a creature.
- Label: False
- Premises:
  1. Beasts of Prey is either a fantasy novel or a science fiction novel.
  2. Science fiction novels are not about mythological creatures
  3. Beasts of Prey Is about a creature known as the Shetani.
  4. Shetanis are mythological.
- Wrong Type: [Type 5: Incorrect answers]

	We know that shetanis are mythological. The hypothesis states that a Shetani is either mythological or a creature. Since we already know that shetanis are mythological, the hypothesis is true.

---
## Story ID: 17	Example ID: 49

- Hypothesis: Amy Odell is an English toy inventor.
- Label: Unknown
- Premises:
  1. Odell is an English surname originating in Odell, Bedfordshire.
  2. In some families Odell is spelled O'Dell, in a mistaken Irish adaptation.
  3. Notable people with the surname include Amy Odell, Jack Odell, and Mats Odell.
  4. Amy Odell is a British singer-songwriter.
  5. Jack Odell is an English toy inventor.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	we know that Amy Odell is a British singer-songwriter and Jack Odell is an English toy inventor. They share the same surname, but there is no information indicating that Amy Odell is an English toy inventor herself. Maybe there is a common knowledge that if someone is a singer-songwriter, he is not a toy inventor. However, it is not provided in the premises.

---
## Story ID: 167	Example ID: 482

- Hypothesis: Mary gets from New Haven to New York City by train.
- Label: False
- Premises:
  1. If you go somewhere by train, you will not lose time.
  2. If you go somewhere by car and meet traffic jam, you will lose time.
  3. If you lose time, you will be late for work.
  4. Mary can get from New Haven to New York City either by train or car.
  5. Mary is late for work.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	we know the following:

1. If Mary goes by car and meets a traffic jam, she will lose time.
2. If Mary loses time, she will be late for work.
3. Mary is late for work.
4. Mary can get from New Haven to New York City either by train or car.
5. If Mary goes by train, she will not lose time.

However, the given information is not sufficient to determine whether Mary gets from New Haven to New York City by train or not. It is only known that she is late for work, but there might be other reasons for her being late besides transportation.

---
## Story ID: 167	Example ID: 483

- Hypothesis: Mary gets from New Haven to New York City by car.
- Label: True
- Premises:
  1. If you go somewhere by train, you will not lose time.
  2. If you go somewhere by car and meet traffic jam, you will lose time.
  3. If you lose time, you will be late for work.
  4. Mary can get from New Haven to New York City either by train or car.
  5. Mary is late for work.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	we know that Mary can get from New Haven to New York City either by train or car. Mary is late for work, and if she loses time, she will be late for work. Additionally, if she goes by car and encounters a traffic jam, she will lose time. However, there is no direct information stating that Mary went by car or experienced a traffic jam. It is also possible that she went by train and was late for another reason.

---
## Story ID: 208	Example ID: 599

- Hypothesis: There is a great lake that did not form at the end of the Last Glacial Period.
- Label: False
- Premises:
  1. The Great Lakes are Lake Superior, Lake Michigan, Lake Huron, Lake Erie, and Lake Ontario.
  2. Some major settlements of Lake Erie are in NY, PA, OH, and MI.
  3. NY, PA, OH, MI are states in the US.
  4. ON is a state of Canada.
  5. There is a major settlement of Lake Huron in ON. 
  6. All states are in their country.
  7. The US is in North America.
  8. The Great Lakes began to form at the end of the Last Glacial Period.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	we know that the Great Lakes are Lake Superior, Lake Michigan, Lake Huron, Lake Erie, and Lake Ontario, and they began to form at the end of the Last Glacial Period. However, there's no information provided about any other great lake that did not form at the end of the Last Glacial Period. Maybe there is a common knowledge that there is no other great lake that did not form at the end of the Last Glacial Period, but it is not provided in the premises.

---
## Story ID: 105	Example ID: 321

- Hypothesis: Hyunsik is Korean.
- Label: Unknown
- Premises:
  1. Show Your Love is a song recorded by the South Korean boy band BtoB 4u.
  2. The lead single of the extended play Inside is Show Your Love.
  3. Show Your Love contains a hopeful message.
  4. BtoB 4u member Hyunsik wrote Show Your Love.
  5. There is a music video for Show Your Love.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	we can deduce that BtoB 4u is a South Korean boy band and Hyunsik is a member of this group. As Hyunsik is part of a South Korean band, it is reasonable to infer that Hyunsik is Korean. However, this deduction is not with certainty. It is possible that Hyunsik is not Korean, but a member of a South Korean band. In addition, Hyunsik is a typical Korean name, but it is not impossible for a non-Korean to have this name.

---
## Story ID: 16	Example ID: 46

- Hypothesis: Dagfinn Dahl is a Norwegian physician.
- Label: Unknown
- Premises:
  1. Dagfinn is a given name.
  2. Notable people with the given name include Dagfinn Aarskog, Dagfinn Bakke and Dagfinn Dahl. 
  3. Dagfinn Aarskog is a Norwegian physician.
  4. Dagfinn Dahl is a Norwegian barrister.
- Wrong Type: [Type 5: Incorrect answers]

	we learn that Dagfinn Aarskog is a Norwegian physician and Dagfinn Dahl is a Norwegian barrister. Since Dagfinn Dahl is specifically identified as a barrister and not a physician, we can conclude that the hypothesis is false.

---
## Story ID: 34	Example ID: 100

- Hypothesis: Nadal is in the Big 3.
- Label: True
- Premises:
  1. Rafa Nadal was born in Mallorca.
  2. Rafa Nadal is a professional tennis player.
  3. Nadal's win ratio is higher than 80%.
  4. All players in the Big 3 are professionals who have a high win ratio.
- Wrong Type: [Type 5: Incorrect answers]

	we know that Rafa Nadal is a professional tennis player and that his win ratio is higher than 80%. We can deduce that Rafa Nadal is a professional tennis player with a high win ratio. However, there's no direct information about Nadal being a part of the Big 3.

---
## Story ID: 49	Example ID: 144

- Hypothesis: Professional wide receivers are good at catching balls.
- Label: Unknown
- Premises:
  1. Quincy McDuffie is an American professional wide receiver in Canadian Football.
  2. People who can catch balls are good wide receivers. 
  3. Quincy McDuffie can catch many footballs easily.
  4. Good wide receivers play professionally.
  5. Good wide receivers can catch with both their left and right hand.
  6. All footballs are balls.
- Wrong Type: [Type 5: Incorrect answers]

	we can deduce that Quincy McDuffie is a professional wide receiver who can catch many footballs easily. The premises also state that people who can catch balls are good wide receivers and good wide receivers play professionally. Thus, it is true that professional wide receivers like Quincy McDuffie are good at catching balls.

---
## Story ID: 102	Example ID: 310

- Hypothesis: Ted Smith was a sergeant.
- Label: Unknown
- Premises:
  1. Edwin Smith was a New Zealand Rower from Auckland.
  2. Edwin Smith was also known as Ted Smith.
  3. Edwin Smith went to Rose Road Primary School, located in Grey Lynn.
  4. Edwin Smith was a sergeant who served with the New Zealand 24th battalion in Italy and Egypt.
  5. Broadway Sheetmetals was a buisness that was ran and owned by Edwin Smith, who was a sheetmetal worker.
- Wrong Type: [Type 5: Incorrect answers]

	we can see that Edwin Smith, who was also known as Ted Smith, was a sergeant who served with the New Zealand 24th battalion in Italy and Egypt. Thus, it is true that Ted Smith was a sergeant.

---
## Story ID: 139	Example ID: 409

- Hypothesis: Jung fought Sadollah.
- Label: Unknown
- Premises:
  1. UFC Fight Night was a mixed martial arts event and was held in Sweden.
  2. At UFC Fight Night, Sadollah was scheduled to fight Musoke.
  3. Sadollah fought Akiyama at UFC Fight Night.
  4. Musoke fought Yakovlev at UFC Fight Night.
  5. Jung was injured at UFC Fight Night.
  6. Injured people did not fight at UFC Fight Night.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	we can deduce the following:

1. Sadollah fought Akiyama at UFC Fight Night.
2. Jung was injured at UFC Fight Night.
3. Injured people did not fight at UFC Fight Night.
4. Sadollah was scheduled to fight Musoke at UFC Fight Night.

Given that Jung was injured and injured people did not fight at UFC Fight Night, we can conclude that Jung did not fight at this event. Moreover, Sadollah fought Akiyama at UFC Fight Night, not Jung. However, Jung could be injured during the fight between Sadollah and Akiyama. Therefore, we cannot confirm that Jung fought Sadollah.

---
## Story ID: 139	Example ID: 411

- Hypothesis: Sadollah fought Musoke.
- Label: Unknown
- Premises:
  1. UFC Fight Night was a mixed martial arts event and was held in Sweden.
  2. At UFC Fight Night, Sadollah was scheduled to fight Musoke.
  3. Sadollah fought Akiyama at UFC Fight Night.
  4. Musoke fought Yakovlev at UFC Fight Night.
  5. Jung was injured at UFC Fight Night.
  6. Injured people did not fight at UFC Fight Night.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	we know that:

1. Sadollah was scheduled to fight Musoke at UFC Fight Night.
2. Musoke fought Yakovlev at UFC Fight Night.
3. Sadollah fought Akiyama at UFC Fight Night.

However, there is no information about whether the scheduled fight between Sadollah and Musoke actually took place or was replaced by the other fights mentioned. Therefore, we cannot confirm that Sadollah fought Musoke.

---
## Story ID: 237	Example ID: 677

- Hypothesis: Hadid became a UK citizen later in her life.
- Label: True
- Premises:
  1. Zaha Hadid is a British-Iraqi architect, artist and designer.
  2. Zaha Hadid was born on 31 October 1950 in Baghdad, Iraq.
  3. Hadid was a visiting professor of Architectural Design at the Yale School of Architecture.
  4. Max is an aspiring architecture student, and he plans to apply to Yale School of Architecture. 
- Wrong Type: [Type 1: Missing common knowledge or contradictory to common knowledge in the premises]

	we find information about Zaha Hadid's career, her being a British-Iraqi architect, artist, and designer, and that she taught at the Yale School of Architecture. However, there is no information about her citizenship history or if she became a UK citizen later in her life. However, if someone knows that Zaha Hadid is a British-Iraqi architect, artist, and designer, it is reasonable to assume that she became a UK citizen later in her life.

---
## Story ID: 237	Example ID: 679

- Hypothesis: Hadid was born in 1982.
- Label: Unknown
- Premises:
  1. Zaha Hadid is a British-Iraqi architect, artist and designer.
  2. Zaha Hadid was born on 31 October 1950 in Baghdad, Iraq.
  3. Hadid was a visiting professor of Architectural Design at the Yale School of Architecture.
  4. Max is an aspiring architecture student, and he plans to apply to Yale School of Architecture. 
- Wrong Type: [Type 1: Missing common knowledge or contradictory to common knowledge in the premises]

	we can see that Zaha Hadid was born on 31 October 1950 in Baghdad, Iraq. This directly contradicts the hypothesis that Hadid was born in 1982. It is common knowledge that people are born only once, and it is impossible for someone to be born in two different years.

---
## Story ID: 194	Example ID: 557

- Hypothesis: Rosa is the daughter of someone who is responsible for the oversight of traffic.
- Label: True
- Premises:
  1. Rosa was born in Santiago. 
  2. Santiago is the capital and largest city of Chile.
  3. Rosa is the daughter of a Catalan building contractor, Jose.
  4. Jose has a Chilean wife, Carmen.
  5. A building contractor is responsible for the day-to-day oversight of a construction site. 
- Wrong Type: [Type 5: Incorrect answers]

	we know that Rosa is the daughter of Jose, a building contractor. However, there is no information connecting Jose's occupation as a building contractor to being responsible for the oversight of traffic. Therefore, we cannot confirm the hypothesis. A building contractor is responsible for the day-to-day oversight of a construction site, not traffic.

---
## Story ID: 136	Example ID: 402

- Hypothesis: Phoenix makes pop rock music.
- Label: False
- Premises:
  1. Phoneix's music is classified under the indie pop genre.
  2. Phoenix is a band from France.
  3. French bands write songs in French or in English.
  4. Aside from indie pop, pop rock and synth-pop are two other genres of music.
  5. Phoneix has no songs in French.
- Wrong Type: [Type 2: Overly ambiguous problems failing to provide unequivocal answers]

	we know that Phoenix is a French band and their music is classified under the indie pop genre. However, there is no direct information about Phoenix making pop rock music. Other genres like pop rock and synth-pop are mentioned but not specified as the genre of Phoenix's music. It is possible that Phoenix makes pop rock music, but it is not certain.
