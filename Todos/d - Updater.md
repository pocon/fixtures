Updater
========

Few parts to this:

## 1. Function on Fixture Class ##

Write a function on the fixture class which takes an input of: ['time', 'location'] and if they don't match up with the current values, call self.team.notify_update() as well as changing the values of that fixture

## 2. Function on Team Class ##

A function, notify(<Boolean: changed>) loops through all subscribers to team and notifies them, by calling subscriber.notify(fixture, <changed>)

## 3. Function on Subscriber ##

notify() which calls all the notification apps if subscriber is subscribed to them ( see (C) for these functions )

