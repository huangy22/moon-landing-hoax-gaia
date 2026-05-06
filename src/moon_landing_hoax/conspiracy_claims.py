"""Conspiracy theory claims and their scientific debunking."""

from gaia.lang import claim, setting, abduction
from .motivation import moon_landing_real, moon_landing_hoax

# ═══════════════════════════════════════════════════════════════════════════
# 1. The Waving Flag
# ═══════════════════════════════════════════════════════════════════════════

lunar_vacuum = setting(
    "The Moon has no atmosphere. In a vacuum there is no air resistance, "
    "so once an object is set in motion it continues to oscillate far longer "
    "than it would on Earth.",
    title="Lunar vacuum environment",
)

obs_flag_waves = claim(
    "In Apollo mission footage and photographs, the American flag planted on the "
    "lunar surface appears to ripple and wave as though blown by wind.",
    title="Observation: flag appears to wave",
)

flag_science = claim(
    "The flag's apparent waving is explained by its Γ-shaped support rod (a "
    "horizontal telescoping arm kept the fabric unfurled) and the absence of air "
    "resistance. When astronauts handled the flagpole, inertial oscillations "
    "persisted far longer than on Earth. In video footage the flag is motionless "
    "except when physically touched.",
    title="Scientific explanation: flag design + vacuum inertia",
)

alt_flag_studio = claim(
    "The flag waves because the footage was shot in an Earth-based studio "
    "with air currents from ventilation or movement of crew.",
    title="Hoax explanation: studio air currents",
)

_s_flag = abduction(
    observation=obs_flag_waves,
    hypothesis=flag_science,
    alternative=alt_flag_studio,
    reason=(
        "The @flag_science explanation is fully consistent with the physics of vacuum "
        "inertia and the known Γ-shaped support rod design. Video analysis confirms "
        "the flag only moves when astronauts touch it — there is no continuous fluttering "
        "as wind would produce. The @alt_flag_studio explanation is contradicted by the "
        "motion pattern: studio air currents would cause continuous random fluttering."
    ),
    background=[lunar_vacuum],
)

# ═══════════════════════════════════════════════════════════════════════════
# 2. No Stars in Photographs
# ═══════════════════════════════════════════════════════════════════════════

obs_no_stars = claim(
    "None of the Apollo mission photographs show stars in the lunar sky, "
    "despite the Moon having no atmosphere to scatter light.",
    title="Observation: no stars in photos",
)

no_stars_science = claim(
    "Stars are absent from Apollo photos because all manned missions landed "
    "during lunar daytime. The sunlit lunar surface has an albedo of ~0.12, "
    "requiring fast shutter speeds (1/125–1/250 s) and small apertures "
    "(f/5.6–f/11) to properly expose the bright foreground. At these camera "
    "settings, stars (apparent magnitude > +1) are far too dim to register "
    "on film. The same effect occurs on Earth: daytime photos rarely show stars.",
    title="Scientific explanation: camera exposure settings",
)

alt_no_stars_studio = claim(
    "Stars are absent because the footage was shot in a studio, and the "
    "backdrop was a simple black curtain without star projections. Accurately "
    "reproducing the star field visible from a specific lunar location would "
    "have been too difficult to fake convincingly.",
    title="Hoax explanation: studio backdrop",
)

_s_stars = abduction(
    observation=obs_no_stars,
    hypothesis=no_stars_science,
    alternative=alt_no_stars_studio,
    reason=(
        "The absence of stars is a well-understood photographic effect. "
        "Any camera set to expose a sunlit landscape will render stars invisible — "
        "this is trivially reproducible on Earth by photographing a nighttime "
        "sports field under floodlights. @no_stars_science provides a complete, "
        "quantitative explanation without invoking a conspiracy. @alt_no_stars_studio "
        "posits an unnecessary and unfalsifiable additional claim."
    ),
)

# ═══════════════════════════════════════════════════════════════════════════
# 3. Van Allen Radiation Belt
# ═══════════════════════════════════════════════════════════════════════════

obs_radiation_belt = claim(
    "The Apollo spacecraft had to pass through the Van Allen radiation belts, "
    "which contain high-energy charged particles trapped by Earth's magnetic field.",
    title="Observation: Apollo transited the Van Allen belts",
)

radiation_safe = claim(
    "Apollo astronauts passed through the Van Allen belts in approximately "
    "30 minutes each way via a trajectory designed to minimize exposure through "
    "the belts' thinnest regions. The total mission radiation dose was measured at "
    "approximately 0.18 rad (1.8 mSv) over the 12-day Apollo 11 mission — "
    "comparable to one or two chest X-rays, and well below the 25 rad threshold "
    "for acute radiation sickness.",
    title="Scientific explanation: minimal radiation dose via fast transit",
)

alt_radiation_lethal = claim(
    "The Van Allen belt radiation would have been lethal to the astronauts, "
    "proving they could not have passed through them and therefore never left "
    "low Earth orbit.",
    title="Hoax explanation: lethal radiation barrier",
)

_s_radiation = abduction(
    observation=obs_radiation_belt,
    hypothesis=radiation_safe,
    alternative=alt_radiation_lethal,
    reason=(
        "The @radiation_safe explanation is backed by dosimetry data from onboard "
        "radiation monitors carried on all Apollo missions. The trajectory was "
        "specifically designed to transit the thinnest regions of the belts quickly. "
        "The @alt_radiation_lethal claim ignores that radiation dose depends on "
        "exposure time and shielding — the aluminum hull provided adequate protection "
        "for the brief transit."
    ),
)

# ═══════════════════════════════════════════════════════════════════════════
# 4. Non-Parallel Shadows
# ═══════════════════════════════════════════════════════════════════════════

obs_shadows = claim(
    "In several Apollo photographs, shadows cast by objects on the lunar surface "
    "appear to point in different directions rather than being parallel.",
    title="Observation: non-parallel shadows",
)

shadows_science = claim(
    "Non-parallel shadows are a well-known perspective effect in wide-angle "
    "photography of uneven terrain. On the Moon's undulating surface, parallel "
    "shadows from a single distant light source (the Sun) appear to diverge when "
    "projected onto a 2D photograph. If multiple artificial light sources existed, "
    "objects would cast multiple shadows — but no Apollo photo shows multiple "
    "shadows from any object.",
    title="Scientific explanation: perspective + uneven terrain",
)

alt_shadows_studio = claim(
    "The non-parallel shadows prove multiple artificial light sources were used "
    "in a studio setting, since a single light source (the Sun) would produce "
    "perfectly parallel shadows.",
    title="Hoax explanation: multiple studio lights",
)

_s_shadows = abduction(
    observation=obs_shadows,
    hypothesis=shadows_science,
    alternative=alt_shadows_studio,
    reason=(
        "@shadows_science explains the effect quantitatively via perspective geometry "
        "on uneven terrain. Crucially, if multiple studio lights existed, each object "
        "would cast multiple shadows — but no Apollo photo shows this. The single-shadow "
        "observation is only consistent with a single distant light source (the Sun). "
        "@alt_shadows_studio fails this basic test."
    ),
)

# ═══════════════════════════════════════════════════════════════════════════
# 5. Footprints Too Clear
# ═══════════════════════════════════════════════════════════════════════════

obs_footprints = claim(
    "Apollo astronaut bootprints on the lunar surface are remarkably sharp and "
    "well-defined, appearing as clear as prints made in wet sand on Earth.",
    title="Observation: sharp footprints in lunar soil",
)

footprints_science = claim(
    "Lunar regolith consists of angular, jagged micro-particles created by "
    "micrometeorite bombardment over billions of years, unlike wind-rounded "
    "Earth sand grains. These angular particles interlock under compression, "
    "holding a sharp imprint without moisture. The effect is analogous to "
    "pressing talcum powder — fine angular powders hold shape without water.",
    title="Scientific explanation: angular regolith holds imprints",
)

alt_footprints_fake = claim(
    "The sharp footprints prove the photos were taken on Earth using wet sand "
    "or a prepared substrate, because dry powder cannot hold such detailed "
    "impressions.",
    title="Hoax explanation: wet sand on Earth",
)

_s_footprints = abduction(
    observation=obs_footprints,
    hypothesis=footprints_science,
    alternative=alt_footprints_fake,
    reason=(
        "@footprints_science is supported by analysis of returned lunar regolith "
        "samples: scanning electron microscopy confirms the angular, interlocking "
        "micro-particle structure. This angular morphology is a direct consequence "
        "of the Moon's lack of atmosphere and water erosion — lunar particles are "
        "never rounded by weathering. @alt_footprints_fake incorrectly assumes "
        "lunar soil behaves like terrestrial sand."
    ),
)

# ═══════════════════════════════════════════════════════════════════════════
# 6. No Blast Crater Under the Lunar Module
# ═══════════════════════════════════════════════════════════════════════════

obs_no_crater = claim(
    "Photos of the Apollo Lunar Module (LM) on the Moon show no significant "
    "blast crater or scorching beneath the descent engine despite the engine "
    "producing ~4,500 kg of thrust during landing.",
    title="Observation: no blast crater under LM",
)

no_crater_science = claim(
    "The absence of a blast crater is explained by three factors: (1) the descent "
    "engine was throttled down to ~1,360 kg of thrust during final approach; "
    "(2) without an atmosphere, exhaust gases expand radially and dissipate rather "
    "than concentrating downward; (3) the lunar surface beneath the LM was swept "
    "clean of loose regolith, which is visible in photos as a lighter-colored area "
    "around the landing site — confirmed by Japan's SELENE probe (2008) and India's "
    "Chandrayaan missions.",
    title="Scientific explanation: low thrust + vacuum gas expansion",
)

alt_crater_studio = claim(
    "The lack of a blast crater proves the Lunar Module was a static prop placed "
    "on a studio floor, because a real rocket landing would create an obvious crater.",
    title="Hoax explanation: LM was a studio prop",
)

_s_crater = abduction(
    observation=obs_no_crater,
    hypothesis=no_crater_science,
    alternative=alt_crater_studio,
    reason=(
        "@no_crater_science is consistent with the physics of rocket exhaust in vacuum "
        "and the known throttle profile of the LM descent engine. The prediction that "
        "loose regolith would be swept outward — rather than cratered — has been "
        "independently confirmed by orbital photographs from Japan (SELENE, 2008) and "
        "India (Chandrayaan) showing lighter disturbed soil around Apollo landing sites. "
        "@alt_crater_studio ignores the difference between atmospheric and vacuum "
        "exhaust behavior."
    ),
)
