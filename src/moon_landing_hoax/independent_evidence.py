"""Independent evidence confirming the Apollo Moon landings."""

from gaia.lang import claim, setting, abduction, induction, noisy_and, deduction
from .motivation import moon_landing_real, moon_landing_hoax

# ═══════════════════════════════════════════════════════════════════════════
# 1. Lunar Laser Retroreflectors
# ═══════════════════════════════════════════════════════════════════════════

retroreflector_background = setting(
    "Apollo 11, 14, and 15 missions deployed corner-cube retroreflector arrays on "
    "the lunar surface. A retroreflector returns any incoming laser beam exactly "
    "back along its incoming direction, regardless of angle of incidence. If pointed "
    "at the correct coordinates, a laser fired from Earth should produce a detectable "
    "return signal concentrated in a narrow time window.",
    title="Retroreflector deployment",
)

obs_retroreflector_us = claim(
    "Since 1969, observatories worldwide have successfully bounced laser pulses "
    "off the Apollo retroreflectors and measured the return signal. When the laser "
    "is aimed at the documented Apollo coordinates, a concentrated burst of photons "
    "returns in a narrow time window. Aiming at nearby coordinates produces no such "
    "concentrated return. Measurements achieve sub-centimeter precision for the "
    "Earth-Moon distance (~384,400 km).",
    title="Laser ranging from Western observatories",
)

obs_retroreflector_china = claim(
    "In January 2018, the Chinese Academy of Sciences' Yunnan Astronomical "
    "Observatory successfully detected return laser pulses from the Apollo 15 "
    "retroreflector using its 1.2 m telescope — the first such detection by China. "
    "In late 2019, Sun Yat-sen University's TianQin Center achieved high-precision "
    "laser ranging to all five lunar retroreflectors (Apollo 11, 14, 15 and "
    "Lunokhod 1, 2), independently confirming their existence and positions.",
    title="Laser ranging from Chinese observatories",
)

alt_retroreflector_unmanned = claim(
    "The retroreflectors could have been placed on the Moon by unmanned probes "
    "without a human landing, similar to the Soviet Lunokhod rovers that also "
    "carried retroreflectors.",
    title="Alternative: unmanned placement of retroreflectors",
)

_s_retro = induction(
    [obs_retroreflector_us, obs_retroreflector_china],
    moon_landing_real,
    alt_exps=[alt_retroreflector_unmanned, alt_retroreflector_unmanned],
    reason=(
        "Multiple independent nations — the US, France, Italy, and China — have "
        "verified the existence of retroreflectors at the documented Apollo landing "
        "sites. @obs_retroreflector_us and @obs_retroreflector_china provide "
        "independent confirmation from geopolitically independent sources. While "
        "@alt_retroreflector_unmanned is logically possible, it would require an "
        "additional conspiracy: NASA secretly launched unmanned missions to place "
        "the retroreflectors while publicly claiming manned landings."
    ),
    background=[retroreflector_background],
)

# ═══════════════════════════════════════════════════════════════════════════
# 2. Lunar Rock Samples
# ═══════════════════════════════════════════════════════════════════════════

obs_moon_rocks = claim(
    "Apollo missions returned 381.7 kg of lunar rock and soil samples from six "
    "landing sites. These samples contain features impossible to produce on Earth: "
    "(1) unoxidized metallic iron microparticles, (2) nano-scale micrometeorite "
    "impact structures, (3) absence of hydrated minerals, (4) cosmic-ray exposure "
    "ages indicating billions of years of surface exposure, (5) the oldest samples "
    "date to 4.5 billion years — 200 million years older than the oldest known "
    "Earth rocks. Over 50 years, thousands of scientists worldwide have studied "
    "these samples in hundreds of laboratories.",
    title="Apollo lunar samples: properties and independent analysis",
)

obs_soviet_samples_match = claim(
    "The Soviet Union's unmanned Luna 16, 20, and 24 missions independently "
    "returned ~300 g of lunar soil. Isotopic analysis of Soviet samples matches "
    "the composition of Apollo samples — both show identical oxygen isotope ratios "
    "and trace element abundances characteristic of a common lunar origin.",
    title="Soviet Luna samples match Apollo samples",
)

obs_china_sample = claim(
    "In 1978, the United States gifted 1 gram of lunar rock to China. Chinese "
    "scientists at the Chinese Academy of Sciences analyzed the sample and "
    "determined it was collected by Apollo 17 (December 1972), based on its "
    "mineral composition and exposure history. The analysis results were published "
    "in peer-reviewed Chinese scientific journals.",
    title="Chinese analysis of gifted Apollo sample",
)

alt_rocks_fake = claim(
    "The lunar rocks were manufactured on Earth or collected from meteorites, "
    "and the analysis results were fabricated or misinterpreted by scientists "
    "worldwide who were either complicit or deceived.",
    title="Alternative: fabricated lunar samples",
)

_s_rocks = induction(
    [obs_moon_rocks, obs_soviet_samples_match, obs_china_sample],
    moon_landing_real,
    alt_exps=[alt_rocks_fake, alt_rocks_fake, alt_rocks_fake],
    reason=(
        "Three independent lines of sample evidence converge: @obs_moon_rocks shows "
        "properties impossible to fake with 1960s technology (and still challenging "
        "today); @obs_soviet_samples_match demonstrates consistency with Soviet "
        "independently-collected samples; @obs_china_sample confirms Chinese scientists' "
        "independent verification. @alt_rocks_fake would require a conspiracy encompassing "
        "thousands of geochemists across dozens of countries over 50+ years."
    ),
)

# ═══════════════════════════════════════════════════════════════════════════
# 3. Third-Party Orbital Imaging
# ═══════════════════════════════════════════════════════════════════════════

obs_lro_images = claim(
    "NASA's Lunar Reconnaissance Orbiter (LRO), launched in 2009, captured "
    "high-resolution photographs of all six Apollo landing sites showing the "
    "Lunar Module descent stages, deployed experiment packages, rover tracks "
    "(Apollo 15–17), and astronaut footpaths — all consistent with documented "
    "mission activities.",
    title="LRO photographs of Apollo landing sites",
)

obs_japan_selene = claim(
    "Japan's SELENE (Kaguya) lunar orbiter in 2008 photographed the Apollo 15 "
    "landing site, detecting a halo of lighter-colored disturbed regolith around "
    "the Lunar Module position. The terrain matched surface photographs taken by "
    "Apollo 15 astronauts from ground level.",
    title="Japan SELENE imaging of Apollo 15 site",
)

obs_india_chandrayaan = claim(
    "India's Chandrayaan-1 (2008) and Chandrayaan-2 (2019) probes independently "
    "detected lighter, disturbed soil signatures around the Apollo 15 landing "
    "site — consistent with engine exhaust sweeping away surface regolith.",
    title="India Chandrayaan imaging of Apollo sites",
)

alt_imaging_fake = claim(
    "The orbital images were fabricated or doctored by the respective space "
    "agencies (NASA, JAXA, ISRO) as part of a coordinated international cover-up.",
    title="Alternative: fabricated orbital images",
)

_s_imaging = induction(
    [obs_lro_images, obs_japan_selene, obs_india_chandrayaan],
    moon_landing_real,
    alt_exps=[alt_imaging_fake, alt_imaging_fake, alt_imaging_fake],
    reason=(
        "Three independent space agencies with independent spacecraft, launch vehicles, "
        "and communication networks all detected physical evidence of Apollo landings. "
        "@obs_lro_images shows detailed hardware and tracks; @obs_japan_selene and "
        "@obs_india_chandrayaan provide independent corroboration from nations with no "
        "political motivation to support NASA's claims. @alt_imaging_fake requires "
        "a conspiracy spanning the US, Japan, and India."
    ),
)

# ═══════════════════════════════════════════════════════════════════════════
# 4. Soviet Union's Implicit Acknowledgment
# ═══════════════════════════════════════════════════════════════════════════

obs_soviet_tracked = claim(
    "The Soviet Union independently tracked the Apollo missions using its own "
    "deep-space communication network. Soviet radar and telemetry systems "
    "monitored the Apollo spacecraft's trajectory from Earth orbit to the Moon "
    "and back. Had the signals originated from Earth orbit rather than the Moon, "
    "this would have been trivially detectable by Soviet tracking stations.",
    title="Soviet independent tracking of Apollo missions",
)

obs_soviet_encyclopedia = claim(
    "The Great Soviet Encyclopedia (3rd edition, 1970–1979) — the official "
    "state-approved reference work — lists the Apollo Moon landings as genuine "
    "historical events. The Soviet Union, despite being locked in a fierce "
    "Cold War space competition, never claimed the landings were faked. "
    "Instead, Soviet officials denied a Moon race had ever existed.",
    title="Soviet Encyclopedia acknowledgment",
)

obs_soviet_luna15 = claim(
    "During Apollo 11's mission in July 1969, the Soviet Union's Luna 15 probe "
    "was simultaneously in lunar orbit. The Soviets proactively shared Luna 15's "
    "orbital parameters with the Americans to avoid a collision — an action that "
    "only makes sense if the Soviets knew Apollo 11 was genuinely at the Moon.",
    title="Soviet Luna 15 coordination with Apollo 11",
)

alt_soviet_complicit = claim(
    "The Soviet Union was complicit in the hoax or was deceived — despite having "
    "independent deep-space tracking capabilities and being the Apollo program's "
    "primary geopolitical rival with every motivation to expose a fraud.",
    title="Alternative: Soviet complicity or deception",
)

_s_soviet = induction(
    [obs_soviet_tracked, obs_soviet_encyclopedia, obs_soviet_luna15],
    moon_landing_real,
    alt_exps=[alt_soviet_complicit, alt_soviet_complicit, alt_soviet_complicit],
    reason=(
        "The Soviet Union had the technical capability, geopolitical motivation, and "
        "intelligence infrastructure to detect and expose a hoax. @obs_soviet_tracked "
        "shows they independently monitored the missions; @obs_soviet_encyclopedia shows "
        "official state acknowledgment; @obs_soviet_luna15 shows active coordination "
        "during Apollo 11. @alt_soviet_complicit requires explaining why the USSR's "
        "greatest Cold War rival would help cover up a fraud that humiliated them."
    ),
)

# ═══════════════════════════════════════════════════════════════════════════
# 5. Scale of the Conspiracy Argument
# ═══════════════════════════════════════════════════════════════════════════

obs_400k_people = claim(
    "The Apollo program employed over 400,000 people across NASA, contractor "
    "companies (North American Aviation, Grumman, MIT Instrumentation Lab, etc.), "
    "and support organizations. An additional ~100,000 people were involved in "
    "independent tracking and communication worldwide.",
    title="400,000+ people involved in Apollo",
)

conspiracy_impossible = claim(
    "A conspiracy involving 400,000+ participants is statistically implausible. "
    "Mathematical modeling of conspiracy longevity (Grimes, 2016, PLOS ONE) shows "
    "that conspiracies involving more than ~1,000 people have an expected exposure "
    "time of less than 4 years. After 55+ years, no credible insider has come "
    "forward with evidence of a hoax.",
    title="Large-scale conspiracy is statistically implausible",
)

_s_scale = noisy_and(
    [obs_400k_people],
    conspiracy_impossible,
    reason=(
        "Based on @obs_400k_people and Grimes' statistical model of conspiracy "
        "viability, the probability of maintaining a conspiracy of this scale for "
        "55+ years without a single credible leak is vanishingly small."
    ),
)

_s_conspiracy_refutes_hoax = noisy_and(
    [conspiracy_impossible],
    moon_landing_real,
    reason=(
        "If a hoax conspiracy of this scale is statistically implausible "
        "(@conspiracy_impossible), then the landings were almost certainly real."
    ),
)

# ═══════════════════════════════════════════════════════════════════════════
# 6. Chinese Chief Scientist's Endorsement
# ═══════════════════════════════════════════════════════════════════════════

obs_ouyang_endorsement = claim(
    "Ouyang Ziyuan (欧阳自远), chief scientist of China's Chang'e lunar exploration "
    "program, publicly stated that 'the scientific community has reached consensus "
    "on the authenticity of the Apollo landings.' He systematically addressed "
    "common conspiracy claims — flag motion, absent stars, shadow directions — "
    "with scientific explanations, leveraging China's own lunar exploration "
    "experience and independent data.",
    title="China's chief lunar scientist endorses Apollo authenticity",
)

_s_ouyang = noisy_and(
    [obs_ouyang_endorsement, obs_china_sample, obs_retroreflector_china],
    moon_landing_real,
    reason=(
        "China has no political allegiance to NASA and operates a fully independent "
        "space program. @obs_ouyang_endorsement represents the scientific judgment of "
        "China's top lunar scientist, backed by @obs_china_sample (independent sample "
        "analysis) and @obs_retroreflector_china (independent laser ranging). This "
        "constitutes a strong, geopolitically independent endorsement."
    ),
)
