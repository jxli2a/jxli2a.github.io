---
layout: page
permalink: /software/
title: Software
nav: true
nav_order: 3
---

### dasio

Reading and basic processing of distributed acoustic sensing (DAS) data. Readers for the main interrogator formats
(ASN OptoDAS, OptaSense QuantX, AP Sensing, Silixa iDAS), a file catalog, a numpy data container and fast band-pass
filtering, with optional ambient-noise cross-correlation and PhaseNet-DAS phase picking.

Python · [Code on GitHub](https://github.com/jxli2a/dasio)

### xcap3d

Moment tensor and depth of a Southern California earthquake from its SCEDC event ID. xcap3d downloads the
seismograms, fits them in the manner of the CAP method with Green's functions from 3-D SPECFEM3D simulations in the
SCEC community velocity model, scans depth and mechanism, and writes the result and an HTML report.

Python · [Manual](https://jxli2a.github.io/xcap3d/) · code available on request

### DAS Array Atlas

An inventory and interactive map of distributed acoustic sensing deployments worldwide, compiled from papers, data
repositories and meeting abstracts. Each array lists its fiber setup, publications, data availability and how its
record was verified, alongside background layers of submarine cables, onshore fiber, volcanoes and recent earthquakes.
Shared with collaborators for now; a public release is planned.

Web · [Atlas](https://atlas.dasmonitor.org) (collaborator login)
