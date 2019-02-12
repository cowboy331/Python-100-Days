import random


class Card(object):
    """一张牌"""

    def __init__(self, suite, face):
       self._suite=suite
       self._face=face

    @property
    def face(self):
        return self._face

    @property
    def suite(self):
        return self._suite

    def __str__(self):
        if self._face==1:
            face_str='A'
        elif self._face==11:
            face_str='J'
        elif self._face==12:
            face_str='Q'
        elif self._face==13:
            face_str='K'
        else:
            face_str=str(self._face)
        return '%s%s'%(self._suite,self._face)

    def __repr__(self):
        return self.__str__()

class Poker(object):
    """一副牌"""

    def __init__(self):
        self._cards=[Card(suite,face)
                     for suite in '♠♥♣♦'
                     for face in range(1,14)]
        self._current=0

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        """洗牌-随机乱序"""
        self._current=0
        random.shuffle(self._cards)

    @property
    def next(self):
        """发牌"""
        card=self._cards[self._current]
        self._current+=1
        return card