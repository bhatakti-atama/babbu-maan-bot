from triggers.lunn_trigger import LunnTeVajjTrigger
from triggers.bhorna_trigger import BhornaTrigger
from triggers.r34_cat_trigger import R34CatTrigger
from triggers.hoes_mad_trigger import HoesMadTrigger
from triggers.jarvis_toto_trigger import JarvisTotoTrigger
from triggers.random_response_trigger import RandomResponseTrigger
triggers = [
    LunnTeVajjTrigger(),
    BhornaTrigger(),
    R34CatTrigger(),
    HoesMadTrigger(),
    JarvisTotoTrigger(),
    RandomResponseTrigger() #put this on bottom always, it should trigger only IF there are no other triggers.
]

