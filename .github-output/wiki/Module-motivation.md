# Module: motivation

### space_race

**QID:** `github:moon_landing_hoax::space_race`
**Type:** setting
**Role:** setting
**Content:** During the Cold War (1957–1972), the United States and the Soviet Union competed in the 'Space Race.' NASA's Apollo program aimed to land humans on the Moon, culminating in Apollo 11 on July 20, 1969. Six Apollo missions (11, 12, 14, 15, 16, 17) successfully landed on the Moon between 1969 and 1972.

### hoax_origin

**QID:** `github:moon_landing_hoax::hoax_origin`
**Type:** setting
**Role:** setting
**Content:** The Moon-landing conspiracy theory originated with Bill Kaysing's 1976 book 'We Never Went to the Moon: America's Thirty Billion Dollar Swindle.' Kaysing held a B.A. in English and worked briefly as a technical writer at Rocketdyne in the 1950s. The theory gained traction through the 2001 Fox TV special 'Conspiracy Theory: Did We Land on the Moon?'

### moon_landing_real

**QID:** `github:moon_landing_hoax::moon_landing_real`
**Type:** claim
**Role:** derived
**Content:** The Apollo Moon landings (1969–1972) were real: NASA astronauts traveled to the Moon, walked on its surface, conducted experiments, and returned safely to Earth. This is supported by the scientific community, multiple independent space agencies, and 381.7 kg of returned lunar samples.
**Belief:** 1.00
**Derived from:** noisy_and
**Premises:** `github:moon_landing_hoax::all_anomalies_explained`
**Derived from:** abduction
**Premises:** `github:moon_landing_hoax::obs_retroreflector_us`, `github:moon_landing_hoax::alt_retroreflector_unmanned`
**Derived from:** abduction
**Premises:** `github:moon_landing_hoax::obs_retroreflector_china`, `github:moon_landing_hoax::alt_retroreflector_unmanned`
**Derived from:** induction
**Premises:** `github:moon_landing_hoax::obs_retroreflector_us`, `github:moon_landing_hoax::obs_retroreflector_china`, `github:moon_landing_hoax::alt_retroreflector_unmanned`, `github:moon_landing_hoax::alt_retroreflector_unmanned`
**Derived from:** abduction
**Premises:** `github:moon_landing_hoax::obs_moon_rocks`, `github:moon_landing_hoax::alt_rocks_fake`
**Derived from:** abduction
**Premises:** `github:moon_landing_hoax::obs_soviet_samples_match`, `github:moon_landing_hoax::alt_rocks_fake`
**Derived from:** abduction
**Premises:** `github:moon_landing_hoax::obs_china_sample`, `github:moon_landing_hoax::alt_rocks_fake`
**Derived from:** induction
**Premises:** `github:moon_landing_hoax::obs_moon_rocks`, `github:moon_landing_hoax::obs_soviet_samples_match`, `github:moon_landing_hoax::obs_china_sample`, `github:moon_landing_hoax::alt_rocks_fake`, `github:moon_landing_hoax::alt_rocks_fake`, `github:moon_landing_hoax::alt_rocks_fake`
**Derived from:** abduction
**Premises:** `github:moon_landing_hoax::obs_lro_images`, `github:moon_landing_hoax::alt_imaging_fake`
**Derived from:** abduction
**Premises:** `github:moon_landing_hoax::obs_japan_selene`, `github:moon_landing_hoax::alt_imaging_fake`
**Derived from:** abduction
**Premises:** `github:moon_landing_hoax::obs_india_chandrayaan`, `github:moon_landing_hoax::alt_imaging_fake`
**Derived from:** induction
**Premises:** `github:moon_landing_hoax::obs_lro_images`, `github:moon_landing_hoax::obs_japan_selene`, `github:moon_landing_hoax::obs_india_chandrayaan`, `github:moon_landing_hoax::alt_imaging_fake`, `github:moon_landing_hoax::alt_imaging_fake`, `github:moon_landing_hoax::alt_imaging_fake`
**Derived from:** abduction
**Premises:** `github:moon_landing_hoax::obs_soviet_tracked`, `github:moon_landing_hoax::alt_soviet_complicit`
**Derived from:** abduction
**Premises:** `github:moon_landing_hoax::obs_soviet_encyclopedia`, `github:moon_landing_hoax::alt_soviet_complicit`
**Derived from:** abduction
**Premises:** `github:moon_landing_hoax::obs_soviet_luna15`, `github:moon_landing_hoax::alt_soviet_complicit`
**Derived from:** induction
**Premises:** `github:moon_landing_hoax::obs_soviet_tracked`, `github:moon_landing_hoax::obs_soviet_encyclopedia`, `github:moon_landing_hoax::obs_soviet_luna15`, `github:moon_landing_hoax::alt_soviet_complicit`, `github:moon_landing_hoax::alt_soviet_complicit`, `github:moon_landing_hoax::alt_soviet_complicit`
**Derived from:** noisy_and
**Premises:** `github:moon_landing_hoax::conspiracy_impossible`
**Derived from:** noisy_and
**Premises:** `github:moon_landing_hoax::obs_ouyang_endorsement`, `github:moon_landing_hoax::obs_china_sample`, `github:moon_landing_hoax::obs_retroreflector_china`
**gaia:** {'provenance': {'referenced_claims': ['all_anomalies_explained', 'alt_imaging_fake', 'alt_retroreflector_unmanned', 'alt_rocks_fake', 'alt_soviet_complicit', 'conspiracy_impossible', 'obs_china_sample', 'obs_india_chandrayaan', 'obs_japan_selene', 'obs_lro_images', 'obs_moon_rocks', 'obs_ouyang_endorsement', 'obs_retroreflector_china', 'obs_retroreflector_us', 'obs_soviet_encyclopedia', 'obs_soviet_luna15', 'obs_soviet_samples_match', 'obs_soviet_tracked']}}
**Referenced by:** unknown -> `github:moon_landing_hoax::real_xor_hoax`

### moon_landing_hoax

**QID:** `github:moon_landing_hoax::moon_landing_hoax`
**Type:** claim
**Role:** independent
**Content:** The Apollo Moon landings were faked: NASA staged the landings in a film studio on Earth to win the Space Race, and all photographic/video evidence was fabricated. The 400,000+ people involved in the Apollo program were either complicit or deceived.
**Prior:** 0.05
**Belief:** 0.00
**Referenced by:** unknown -> `github:moon_landing_hoax::real_xor_hoax`

### real_xor_hoax

**QID:** `github:moon_landing_hoax::real_xor_hoax`
**Type:** claim
**Role:** structural
**Content:** opposite_truth(A, B)
**Belief:** 1.00
**helper_kind:** complement_result
