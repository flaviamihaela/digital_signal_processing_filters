# digital_signal_processing_filters

These applications provide a graphical user interface (GUI) for applying a Finite Impulse Response (FIR) filter to WAV audio files and Infinite Impulse Response (IIR) filter respectively. Users can select a WAV file, import FIR/ IIR coefficients, apply the filter to the audio, and save the filtered audio back into a WAV file format.

## Key aspects:
Features
 - Load WAV audio files for processing.
 - Import filter coefficients from a file. 
 - Apply filter to the audio data. 
 - Save the filtered audio as a new WAV file.

## Technical Details - characteristics of an FIR filter:

 - Impulse Response: FIR filters are defined by their impulse response, which is finite because it settles to zero in a finite amount of time. This property is derived from the filter coefficients, which represent the impulse response directly.

 - Filter Coefficients: The filter coefficients determine the filter's frequency response. These coefficients are used in the convolution process with the input signal to produce the filtered output.

 - Stability: FIR filters are inherently stable, as they do not rely on feedback mechanisms. The absence of feedback loops means that the filter's poles are located at the origin in the z-plane, ensuring stability.

 - Poles: Values in the z-domain (for digital filters) where the filter's transfer function becomes infinite. The position of poles is crucial in determining the filter's stability and frequency response. FIR filters, by design, do not have poles other than at the origin, which contributes to their inherent stability.

## Technical Details - characteristics of an IIR filter:

 - Poles and Zeros: The behavior of an IIR filter is defined by its poles and zeros. Zeros are the roots of the numerator polynomial in the filter's transfer function, and they represent frequencies that the filter attenuates. Poles are the roots of the denominator polynomial, and they determine the filter's stability and resonance.

 - Feedback Mechanism: The presence of poles (due to the feedback mechanism) makes the design and stability analysis of IIR filters more complex compared to FIR filters. The location of poles in the z-plane directly affects the stability; for the filter to be stable, all poles must lie inside the unit circle.

 - Filter Coefficients: The filter coefficients are derived from the poles and zeros and dictate the filter's frequency and phase response. These coefficients are crucial in the filter design and must be chosen carefully to meet specific filtering criteria.

## Applying FIR filter:
It involves convoluting the audio signal with the FIR filter's impulse response, a process which alters the frequency content of the audio signal, enhancing or attenuating specific frequency components based on the filter's design. To prevent circular convolution and to ensure that the output signal is of the desired length, the input signal is often padded, usually with zeros, before convolution with the filter.

## Applying IIR filter 
It involves a recursive algorithm where past output samples are used along with current and past input samples to calculate the new output. This process is sensitive to coefficient quantization, which can significantly affect the filter's stability and performance. Audio signal is normalized before processing to prevent overflow and ensure that the filter operates within its linear range.


