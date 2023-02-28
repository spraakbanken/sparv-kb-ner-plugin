# Comparison between KBNER and SWENER

Example text: [Ikea example](./texts/ikea-example.txt)

Runtime for KBNER: 21 s

Runtime for SWENER: 54 s

```diff


7,9c7
<     <ne ex="ENAMEX" subtype="CRP" type="ORG">
<       <token word="Ikea" pos="PM">Ikea</token>
<     </ne>
---
>     <token word="Ikea" kb-ne="ORG" pos="PM">Ikea</token>
12,14c10
<     <ne ex="ENAMEX" subtype="CRP" type="ORG">
<       <token word="Ikea" pos="PM">Ikea</token>
<     </ne>
---
>     <token word="Ikea" kb-ne="ORG" pos="PM">Ikea</token>
22,30c18,22
<     <ne ex="ENAMEX" subtype="HUM" type="PRS">
<       <token word="Ingvar" pos="PM">Ingvar</token>
<       <token word="Kamprad" pos="PM">Kamprad</token>
<       <token word="Elmtaryd" pos="PM">Elmtaryd</token>
<     </ne>
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Agunnaryd" pos="PM">Agunnaryd</token>
<     </ne>
<     <token word=")" pos="PAD">)</token>
---
>     <token word="Ingvar" kb-ne="PER" pos="PM">Ingvar</token>
>     <token word="Kamprad" kb-ne="PER" pos="PM">Kamprad</token>
>     <token word="Elmtaryd" kb-ne="PER" pos="PM">Elmtaryd</token>
>     <token word="Agunnaryd" pos="PM">Agunnaryd</token>
>     <token word=")" kb-ne="LOC" pos="PAD">)</token>
37,45c29,33
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="1943" pos="RG">1943</token>
<     </ne>
<     <token word="av" pos="PP">av</token>
<     <ne ex="ENAMEX" subtype="HUM" type="PRS">
<       <token word="Ingvar" pos="PM">Ingvar</token>
<       <token word="Kamprad" pos="PM">Kamprad</token>
<     </ne>
<     <token word="." pos="MAD">.</token>
---
>     <token word="1943" pos="RG">1943</token>
>     <token word="av" kb-ne="TME" pos="PP">av</token>
>     <token word="Ingvar" pos="PM">Ingvar</token>
>     <token word="Kamprad" kb-ne="PER" pos="PM">Kamprad</token>
>     <token word="." kb-ne="PER" pos="MAD">.</token>
54,56c42
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Nederländerna" pos="PM">Nederländerna</token>
<     </ne>
---
>     <token word="Nederländerna" kb-ne="LOC" pos="PM">Nederländerna</token>
64,70c50,52
<     <ne ex="ENAMEX" subtype="CRP" type="ORG">
<       <token word="Interogo" pos="PM">Interogo</token>
<     </ne>
<     <token word="i" pos="PP">i</token>
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Luxemburg" pos="PM">Luxemburg</token>
<     </ne>
---
>     <token word="Interogo" kb-ne="ORG" pos="PM">Interogo</token>
>     <token word="i" pos="PP">i</token>
>     <token word="Luxemburg" kb-ne="LOC" pos="PM">Luxemburg</token>
77,79c59
<     <ne ex="ENAMEX" subtype="HUM" type="PRS">
<       <token word="Kamprad" pos="PM">Kamprad</token>
<     </ne>
---
>     <token word="Kamprad" kb-ne="PER" pos="PM">Kamprad</token>
84,87c64,65
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="verksamhetsåret" pos="NN">verksamhetsåret</token>
<       <token word="2012" pos="RG">2012</token>
<     </ne>
---
>     <token word="verksamhetsåret" kb-ne="TME" pos="NN">verksamhetsåret</token>
>     <token word="2012" kb-ne="TME" pos="RG">2012</token>
89,95c67,71
<     <token word="Ikeakoncernen" pos="NN">Ikeakoncernen</token>
<     <ne ex="NUMEX" subtype="CUR" type="MSR">
<       <token word="241" pos="RG">241</token>
<       <token word="miljarder" pos="NN">miljarder</token>
<       <token word="kronor" pos="NN">kronor</token>
<     </ne>
<     <token word="." pos="MAD">.</token>
---
>     <token word="Ikeakoncernen" kb-ne="ORG" pos="NN">Ikeakoncernen</token>
>     <token word="241" pos="RG">241</token>
>     <token word="miljarder" kb-ne="MSR" pos="NN">miljarder</token>
>     <token word="kronor" kb-ne="MSR" pos="NN">kronor</token>
>     <token word="." kb-ne="MSR" pos="MAD">.</token>
113,115c89
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Sverige" pos="PM">Sverige</token>
<     </ne>
---
>     <token word="Sverige" kb-ne="LOC" pos="PM">Sverige</token>
118,120c92
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Helsingborg" pos="PM">Helsingborg</token>
<     </ne>
---
>     <token word="Helsingborg" kb-ne="LOC" pos="PM">Helsingborg</token>
125,127c97
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Helsingborg" pos="PM">Helsingborg</token>
<     </ne>
---
>     <token word="Helsingborg" kb-ne="LOC" pos="PM">Helsingborg</token>
129,131c99
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="idag" pos="AB">idag</token>
<     </ne>
---
>     <token word="idag" kb-ne="TME" pos="AB">idag</token>
159,166c127,130
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Malmö" pos="PM">Malmö</token>
<     </ne>
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="1" pos="RO">1</token>
<       <token word="september" pos="NN">september</token>
<       <token word="2015" pos="RG">2015</token>
<     </ne>
---
>     <token word="Malmö" kb-ne="LOC" pos="PM">Malmö</token>
>     <token word="1" kb-ne="TME" pos="RO">1</token>
>     <token word="september" kb-ne="TME" pos="NN">september</token>
>     <token word="2015" kb-ne="TME" pos="RG">2015</token>
180,181c144,145
<     <token word="Vintrie" pos="PM">Vintrie</token>
<     <token word="park" pos="NN">park</token>
---
>     <token word="Vintrie" kb-ne="LOC" pos="PM">Vintrie</token>
>     <token word="park" kb-ne="LOC" pos="NN">park</token>
185,187c149
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Svågertorp" pos="PM">Svågertorp</token>
<     </ne>
---
>     <token word="Svågertorp" kb-ne="LOC" pos="PM">Svågertorp</token>
216,218c178
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Mellanöstern" pos="PM">Mellanöstern</token>
<     </ne>
---
>     <token word="Mellanöstern" kb-ne="LOC" pos="PM">Mellanöstern</token>
220,221c180,181
<     <token word="spanska" pos="JJ">spanska</token>
<     <token word="öarna" pos="NN">öarna</token>
---
>     <token word="spanska" kb-ne="LOC" pos="JJ">spanska</token>
>     <token word="öarna" kb-ne="LOC" pos="NN">öarna</token>
237,267c197,211
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Tyskland" pos="PM">Tyskland</token>
<     </ne>
<     <ne ex="NUMEX" subtype="PRC" type="MSR">
<       <token word="16" pos="RG">16</token>
<       <token word="%" pos="NN">%</token>
<     </ne>
<     <token word="," pos="MID">,</token>
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="USA" pos="PM">USA</token>
<     </ne>
<     <ne ex="NUMEX" subtype="PRC" type="MSR">
<       <token word="11" pos="RG">11</token>
<       <token word="%" pos="NN">%</token>
<     </ne>
<     <token word="," pos="MID">,</token>
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Frankrike" pos="PM">Frankrike</token>
<     </ne>
<     <ne ex="NUMEX" subtype="PRC" type="MSR">
<       <token word="10" pos="RG">10</token>
<       <token word="%" pos="NN">%</token>
<     </ne>
<     <token word="," pos="MID">,</token>
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Storbritannien" pos="PM">Storbritannien</token>
<     </ne>
<     <ne ex="NUMEX" subtype="PRC" type="MSR">
<       <token word="7" pos="RG">7</token>
<       <token word="%" pos="NN">%</token>
<     </ne>
---
>     <token word="Tyskland" kb-ne="LOC" pos="PM">Tyskland</token>
>     <token word="16" kb-ne="MSR" pos="RG">16</token>
>     <token word="%" kb-ne="MSR" pos="NN">%</token>
>     <token word="," pos="MID">,</token>
>     <token word="USA" kb-ne="LOC" pos="PM">USA</token>
>     <token word="11" kb-ne="MSR" pos="RG">11</token>
>     <token word="%" kb-ne="MSR" pos="NN">%</token>
>     <token word="," pos="MID">,</token>
>     <token word="Frankrike" kb-ne="LOC" pos="PM">Frankrike</token>
>     <token word="10" kb-ne="MSR" pos="RG">10</token>
>     <token word="%" kb-ne="MSR" pos="NN">%</token>
>     <token word="," pos="MID">,</token>
>     <token word="Storbritannien" kb-ne="LOC" pos="PM">Storbritannien</token>
>     <token word="7" kb-ne="MSR" pos="RG">7</token>
>     <token word="%" kb-ne="MSR" pos="NN">%</token>
269,275c213,215
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Italien" pos="PM">Italien</token>
<     </ne>
<     <ne ex="NUMEX" subtype="PRC" type="MSR">
<       <token word="7" pos="RG">7</token>
<       <token word="%" pos="NN">%</token>
<     </ne>
---
>     <token word="Italien" kb-ne="LOC" pos="PM">Italien</token>
>     <token word="7" kb-ne="MSR" pos="RG">7</token>
>     <token word="%" kb-ne="MSR" pos="NN">%</token>
280,282c220
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Sverige" pos="PM">Sverige</token>
<     </ne>
---
>     <token word="Sverige" kb-ne="LOC" pos="PM">Sverige</token>
294,301c232,235
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Borlänge" pos="PM">Borlänge</token>
<     </ne>
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="25" pos="RG">25</token>
<       <token word="oktober" pos="NN">oktober</token>
<       <token word="2013" pos="RG">2013</token>
<     </ne>
---
>     <token word="Borlänge" kb-ne="LOC" pos="PM">Borlänge</token>
>     <token word="25" kb-ne="TME" pos="RG">25</token>
>     <token word="oktober" kb-ne="TME" pos="NN">oktober</token>
>     <token word="2013" kb-ne="TME" pos="RG">2013</token>
308,310c242
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="dessförinnan" pos="AB">dessförinnan</token>
<     </ne>
---
>     <token word="dessförinnan" kb-ne="TME" pos="AB">dessförinnan</token>
314,322c246,250
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Uddevalla" pos="PM">Uddevalla</token>
<     </ne>
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="den" pos="DT">den</token>
<       <token word="8" pos="RO">8</token>
<       <token word="maj" pos="NN">maj</token>
<       <token word="2013" pos="RG">2013</token>
<     </ne>
---
>     <token word="Uddevalla" kb-ne="LOC" pos="PM">Uddevalla</token>
>     <token word="den" kb-ne="TME" pos="DT">den</token>
>     <token word="8" kb-ne="TME" pos="RO">8</token>
>     <token word="maj" kb-ne="TME" pos="NN">maj</token>
>     <token word="2013" kb-ne="TME" pos="RG">2013</token>
325,330c253,256
<     <ne ex="NUMEX" subtype="MSU" type="MSR">
<       <token word="på" pos="PP">på</token>
<       <token word="37" pos="RG">37</token>
<       <token word="400" pos="RG">400</token>
<       <token word="kvadratmeter" pos="NN">kvadratmeter</token>
<     </ne>
---
>     <token word="på" pos="PP">på</token>
>     <token word="37" kb-ne="MSR" pos="RG">37</token>
>     <token word="400" kb-ne="MSR" pos="RG">400</token>
>     <token word="kvadratmeter" kb-ne="MSR" pos="NN">kvadratmeter</token>
336,338c262
<     <ne ex="ENAMEX" subtype="GPL" type="LOC">
<       <token word="Ikea" pos="PM">Ikea</token>
<     </ne>
---
>     <token word="Ikea" kb-ne="ORG" pos="PM">Ikea</token>
341,347c265,267
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Haparanda" pos="PM">Haparanda</token>
<     </ne>
<     <token word="i" pos="PP">i</token>
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Sverige" pos="PM">Sverige</token>
<     </ne>
---
>     <token word="Haparanda" kb-ne="LOC" pos="PM">Haparanda</token>
>     <token word="i" pos="PP">i</token>
>     <token word="Sverige" kb-ne="LOC" pos="PM">Sverige</token>
352,354c272
<     <ne ex="ENAMEX" subtype="PPL" type="LOC">
<       <token word="Finland" pos="PM">Finland</token>
<     </ne>
---
>     <token word="Finland" kb-ne="LOC" pos="PM">Finland</token>
356c274
<     <token word="HaparandaTornio" pos="PM">HaparandaTornio</token>
---
>     <token word="HaparandaTornio" kb-ne="LOC" pos="PM">HaparandaTornio</token>
361,363c279
<     <ne ex="ENAMEX" subtype="CRP" type="ORG">
<       <token word="Ikea" pos="PM">Ikea</token>
<     </ne>
---
>     <token word="Ikea" kb-ne="ORG" pos="PM">Ikea</token>
366,368c282
<     <ne ex="ENAMEX" subtype="GPL" type="LOC">
<       <token word="Moskva" pos="PM">Moskva</token>
<     </ne>
---
>     <token word="Moskva" kb-ne="LOC" pos="PM">Moskva</token>
370,373c284,285
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="år" pos="NN">år</token>
<       <token word="2005" pos="RG">2005</token>
<     </ne>
---
>     <token word="år" kb-ne="TME" pos="NN">år</token>
>     <token word="2005" kb-ne="TME" pos="RG">2005</token>
386,388c298
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="Samtidigt" pos="AB">Samtidigt</token>
<     </ne>
---
>     <token word="Samtidigt" kb-ne="TME" pos="AB">Samtidigt</token>
390,392c300
<     <ne ex="ENAMEX" subtype="CRP" type="ORG">
<       <token word="Ikea" pos="PM">Ikea</token>
<     </ne>
---
>     <token word="Ikea" kb-ne="ORG" pos="PM">Ikea</token>
395,397c303
<     <ne ex="ENAMEX" subtype="GPL" type="LOC">
<       <token word="Moskva" pos="PM">Moskva</token>
<     </ne>
---
>     <token word="Moskva" kb-ne="LOC" pos="PM">Moskva</token>
404,405c310,311
<     <token word="Sjeremetievo" pos="PM">Sjeremetievo</token>
<     <token word="internationella" pos="JJ">internationella</token>
---
>     <token word="Sjeremetievo" kb-ne="LOC" pos="PM">Sjeremetievo</token>
>     <token word="internationella" kb-ne="LOC" pos="JJ">internationella</token>
416,418c322
<     <ne ex="ENAMEX" subtype="CRP" type="ORG">
<       <token word="Ikea" pos="PM">Ikea</token>
<     </ne>
---
>     <token word="Ikea" kb-ne="ORG" pos="PM">Ikea</token>
461c365
<     <token word="Ikeas" pos="PM">Ikeas</token>
---
>     <token word="Ikeas" kb-ne="ORG" pos="PM">Ikeas</token>
514,521c418,421
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="varje" pos="DT">varje</token>
<       <token word="år" pos="NN">år</token>
<     </ne>
<     <ne ex="TIMEX" subtype="DAT" type="TME">
<       <token word="i" pos="PP">i</token>
<       <token word="augusti" pos="NN">augusti</token>
<     </ne>
---
>     <token word="varje" kb-ne="TME" pos="DT">varje</token>
>     <token word="år" kb-ne="TME" pos="NN">år</token>
>     <token word="i" kb-ne="TME" pos="PP">i</token>
>     <token word="augusti" kb-ne="TME" pos="NN">augusti</token>
```
