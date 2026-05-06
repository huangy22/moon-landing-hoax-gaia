# Module: conspiracy_claims

### lunar_vacuum

**QID:** `github:moon_landing_hoax::lunar_vacuum`
**Type:** setting
**Role:** setting
**Content:** The Moon has no atmosphere. In a vacuum there is no air resistance, so once an object is set in motion it continues to oscillate far longer than it would on Earth.

### obs_flag_waves

**QID:** `github:moon_landing_hoax::obs_flag_waves`
**Type:** claim
**Role:** independent
**Content:** In Apollo mission footage and photographs, the American flag planted on the lunar surface appears to ripple and wave as though blown by wind.
**Prior:** 0.95
**Belief:** 1.00
**Referenced by:** abduction -> `github:moon_landing_hoax::flag_science`

### flag_science

**QID:** `github:moon_landing_hoax::flag_science`
**Type:** claim
**Role:** derived
**Content:** The flag's apparent waving is explained by its Γ-shaped support rod (a horizontal telescoping arm kept the fabric unfurled) and the absence of air resistance. When astronauts handled the flagpole, inertial oscillations persisted far longer than on Earth. In video footage the flag is motionless except when physically touched.
**Belief:** 1.00
**Derived from:** abduction
**Premises:** `github:moon_landing_hoax::obs_flag_waves`, `github:moon_landing_hoax::alt_flag_studio`
**gaia:** {'provenance': {'referenced_claims': ['alt_flag_studio', 'flag_science']}}
**Referenced by:** noisy_and -> `github:moon_landing_hoax::all_anomalies_explained`

### alt_flag_studio

**QID:** `github:moon_landing_hoax::alt_flag_studio`
**Type:** claim
**Role:** independent
**Content:** The flag waves because the footage was shot in an Earth-based studio with air currents from ventilation or movement of crew.
**Prior:** 0.05
**Belief:** 0.05
**Referenced by:** abduction -> `github:moon_landing_hoax::flag_science`

### obs_no_stars

**QID:** `github:moon_landing_hoax::obs_no_stars`
**Type:** claim
**Role:** independent
**Content:** None of the Apollo mission photographs show stars in the lunar sky, despite the Moon having no atmosphere to scatter light.
**Prior:** 0.95
**Belief:** 1.00
**Referenced by:** abduction -> `github:moon_landing_hoax::no_stars_science`

### no_stars_science

**QID:** `github:moon_landing_hoax::no_stars_science`
**Type:** claim
**Role:** derived
**Content:** Stars are absent from Apollo photos because all manned missions landed during lunar daytime. The sunlit lunar surface has an albedo of ~0.12, requiring fast shutter speeds (1/125–1/250 s) and small apertures (f/5.6–f/11) to properly expose the bright foreground. At these camera settings, stars (apparent magnitude > +1) are far too dim to register on film. The same effect occurs on Earth: daytime photos rarely show stars.
**Belief:** 1.00
**Derived from:** abduction
**Premises:** `github:moon_landing_hoax::obs_no_stars`, `github:moon_landing_hoax::alt_no_stars_studio`
**gaia:** {'provenance': {'referenced_claims': ['alt_no_stars_studio', 'no_stars_science']}}
**Referenced by:** noisy_and -> `github:moon_landing_hoax::all_anomalies_explained`

### alt_no_stars_studio

**QID:** `github:moon_landing_hoax::alt_no_stars_studio`
**Type:** claim
**Role:** independent
**Content:** Stars are absent because the footage was shot in a studio, and the backdrop was a simple black curtain without star projections. Accurately reproducing the star field visible from a specific lunar location would have been too difficult to fake convincingly.
**Prior:** 0.05
**Belief:** 0.05
**Referenced by:** abduction -> `github:moon_landing_hoax::no_stars_science`

### obs_radiation_belt

**QID:** `github:moon_landing_hoax::obs_radiation_belt`
**Type:** claim
**Role:** independent
**Content:** The Apollo spacecraft had to pass through the Van Allen radiation belts, which contain high-energy charged particles trapped by Earth's magnetic field.
**Prior:** 0.99
**Belief:** 1.00
**Referenced by:** abduction -> `github:moon_landing_hoax::radiation_safe`

### radiation_safe

**QID:** `github:moon_landing_hoax::radiation_safe`
**Type:** claim
**Role:** derived
**Content:** Apollo astronauts passed through the Van Allen belts in approximately 30 minutes each way via a trajectory designed to minimize exposure through the belts' thinnest regions. The total mission radiation dose was measured at approximately 0.18 rad (1.8 mSv) over the 12-day Apollo 11 mission — comparable to one or two chest X-rays, and well below the 25 rad threshold for acute radiation sickness.
**Belief:** 1.00
**Derived from:** abduction
**Premises:** `github:moon_landing_hoax::obs_radiation_belt`, `github:moon_landing_hoax::alt_radiation_lethal`
**gaia:** {'provenance': {'referenced_claims': ['alt_radiation_lethal', 'radiation_safe']}}
**Referenced by:** noisy_and -> `github:moon_landing_hoax::all_anomalies_explained`

### alt_radiation_lethal

**QID:** `github:moon_landing_hoax::alt_radiation_lethal`
**Type:** claim
**Role:** independent
**Content:** The Van Allen belt radiation would have been lethal to the astronauts, proving they could not have passed through them and therefore never left low Earth orbit.
**Prior:** 0.02
**Belief:** 0.02
**Referenced by:** abduction -> `github:moon_landing_hoax::radiation_safe`

### obs_shadows

**QID:** `github:moon_landing_hoax::obs_shadows`
**Type:** claim
**Role:** independent
**Content:** In several Apollo photographs, shadows cast by objects on the lunar surface appear to point in different directions rather than being parallel.
**Prior:** 0.90
**Belief:** 1.00
**Referenced by:** abduction -> `github:moon_landing_hoax::shadows_science`

### shadows_science

**QID:** `github:moon_landing_hoax::shadows_science`
**Type:** claim
**Role:** derived
**Content:** Non-parallel shadows are a well-known perspective effect in wide-angle photography of uneven terrain. On the Moon's undulating surface, parallel shadows from a single distant light source (the Sun) appear to diverge when projected onto a 2D photograph. If multiple artificial light sources existed, objects would cast multiple shadows — but no Apollo photo shows multiple shadows from any object.
**Belief:** 1.00
**Derived from:** abduction
**Premises:** `github:moon_landing_hoax::obs_shadows`, `github:moon_landing_hoax::alt_shadows_studio`
**gaia:** {'provenance': {'referenced_claims': ['alt_shadows_studio', 'shadows_science']}}
**Referenced by:** noisy_and -> `github:moon_landing_hoax::all_anomalies_explained`

### alt_shadows_studio

**QID:** `github:moon_landing_hoax::alt_shadows_studio`
**Type:** claim
**Role:** independent
**Content:** The non-parallel shadows prove multiple artificial light sources were used in a studio setting, since a single light source (the Sun) would produce perfectly parallel shadows.
**Prior:** 0.03
**Belief:** 0.03
**Referenced by:** abduction -> `github:moon_landing_hoax::shadows_science`

### obs_footprints

**QID:** `github:moon_landing_hoax::obs_footprints`
**Type:** claim
**Role:** independent
**Content:** Apollo astronaut bootprints on the lunar surface are remarkably sharp and well-defined, appearing as clear as prints made in wet sand on Earth.
**Prior:** 0.95
**Belief:** 1.00
**Referenced by:** abduction -> `github:moon_landing_hoax::footprints_science`

### footprints_science

**QID:** `github:moon_landing_hoax::footprints_science`
**Type:** claim
**Role:** derived
**Content:** Lunar regolith consists of angular, jagged micro-particles created by micrometeorite bombardment over billions of years, unlike wind-rounded Earth sand grains. These angular particles interlock under compression, holding a sharp imprint without moisture. The effect is analogous to pressing talcum powder — fine angular powders hold shape without water.
**Belief:** 1.00
**Derived from:** abduction
**Premises:** `github:moon_landing_hoax::obs_footprints`, `github:moon_landing_hoax::alt_footprints_fake`
**gaia:** {'provenance': {'referenced_claims': ['alt_footprints_fake', 'footprints_science']}}
**Referenced by:** noisy_and -> `github:moon_landing_hoax::all_anomalies_explained`

### alt_footprints_fake

**QID:** `github:moon_landing_hoax::alt_footprints_fake`
**Type:** claim
**Role:** independent
**Content:** The sharp footprints prove the photos were taken on Earth using wet sand or a prepared substrate, because dry powder cannot hold such detailed impressions.
**Prior:** 0.05
**Belief:** 0.05
**Referenced by:** abduction -> `github:moon_landing_hoax::footprints_science`

### obs_no_crater

**QID:** `github:moon_landing_hoax::obs_no_crater`
**Type:** claim
**Role:** independent
**Content:** Photos of the Apollo Lunar Module (LM) on the Moon show no significant blast crater or scorching beneath the descent engine despite the engine producing ~4,500 kg of thrust during landing.
**Prior:** 0.95
**Belief:** 1.00
**Referenced by:** abduction -> `github:moon_landing_hoax::no_crater_science`

### no_crater_science

**QID:** `github:moon_landing_hoax::no_crater_science`
**Type:** claim
**Role:** derived
**Content:** The absence of a blast crater is explained by three factors: (1) the descent engine was throttled down to ~1,360 kg of thrust during final approach; (2) without an atmosphere, exhaust gases expand radially and dissipate rather than concentrating downward; (3) the lunar surface beneath the LM was swept clean of loose regolith, which is visible in photos as a lighter-colored area around the landing site — confirmed by Japan's SELENE probe (2008) and India's Chandrayaan missions.
**Belief:** 1.00
**Derived from:** abduction
**Premises:** `github:moon_landing_hoax::obs_no_crater`, `github:moon_landing_hoax::alt_crater_studio`
**gaia:** {'provenance': {'referenced_claims': ['alt_crater_studio', 'no_crater_science']}}
**Referenced by:** noisy_and -> `github:moon_landing_hoax::all_anomalies_explained`

### alt_crater_studio

**QID:** `github:moon_landing_hoax::alt_crater_studio`
**Type:** claim
**Role:** independent
**Content:** The lack of a blast crater proves the Lunar Module was a static prop placed on a studio floor, because a real rocket landing would create an obvious crater.
**Prior:** 0.03
**Belief:** 0.03
**Referenced by:** abduction -> `github:moon_landing_hoax::no_crater_science`

### all_anomalies_explained

**QID:** `github:moon_landing_hoax::all_anomalies_explained`
**Type:** claim
**Role:** derived
**Content:** All six photographic/video anomalies cited by conspiracy theorists — the waving flag, absent stars, Van Allen radiation, non-parallel shadows, sharp footprints, and missing blast crater — have complete scientific explanations consistent with the known lunar environment. None requires invoking a studio or fabrication.
**Belief:** 1.00
**Derived from:** noisy_and
**Premises:** `github:moon_landing_hoax::flag_science`, `github:moon_landing_hoax::no_stars_science`, `github:moon_landing_hoax::radiation_safe`, `github:moon_landing_hoax::shadows_science`, `github:moon_landing_hoax::footprints_science`, `github:moon_landing_hoax::no_crater_science`
**gaia:** {'provenance': {'referenced_claims': ['flag_science', 'footprints_science', 'no_crater_science', 'no_stars_science', 'radiation_safe', 'shadows_science']}}
**Referenced by:** noisy_and -> `github:moon_landing_hoax::moon_landing_real`
