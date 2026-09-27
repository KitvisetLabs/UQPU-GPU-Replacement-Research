"""SCM-3A authenticated finite-symbol channel accounting.

This module scores a predeclared symbol channel after challenge/reveal. It does
not identify a source and does not establish cross-realm communication.
"""
from __future__ import annotations
from dataclasses import dataclass
import math

@dataclass(frozen=True)
class SymbolChannelResult:
    trials:int; alphabet_size:int; correct:int; erasures:int; elapsed_seconds:float
    evidence_class:str="MODEL_PROTOCOL_ONLY_NO_SOURCE_IDENTITY"

    @property
    def error_count(self): return self.trials-self.correct-self.erasures
    @property
    def symbol_error_rate(self):
        decided=self.trials-self.erasures
        return self.error_count/decided if decided else 0.0
    @property
    def verified_bits_upper_account(self):
        chance=self.trials/self.alphabet_size
        return max(0.0,self.correct-chance)*math.log2(self.alphabet_size)
    @property
    def verified_bit_rate_upper_account(self):
        return self.verified_bits_upper_account/self.elapsed_seconds if self.elapsed_seconds>0 else 0.0

def validate_result(r:SymbolChannelResult)->tuple[str,...]:
    e=[]
    if r.trials<=0:e.append("invalid:trials")
    if r.alphabet_size<2:e.append("invalid:alphabet_size")
    if min(r.correct,r.erasures)<0 or r.correct+r.erasures>r.trials:e.append("invalid:counts")
    if r.elapsed_seconds<=0:e.append("invalid:elapsed_seconds")
    return tuple(e)
