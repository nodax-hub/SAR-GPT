import numpy as np

from DataInput.AntennaParameters import AntennaParameters
from DataInput.Scene import Scene, SceneObject
from DataInput.SignalParameters import SignalParameters
from DocumentationAndReporting.ReportGenerator import ReportGenerator
from PostProcessing.PostProcessingModule import PostProcessingModule
from Propagation.WavePropagationSimulator import WavePropagationSimulator
from ReflectionAndReception.ReceiverSimulator import ReceiverSimulator
from ReflectionAndReception.ReflectionCalculator import ReflectionCalculator
from SignalGeneration.SignalSimulator import SignalSimulator
from SignalProcessing.SignalProcessingModule import SignalProcessingModule
from VerificationAndTesting.VerificationModule import VerificationModule


def main():
    # Задание параметров
    signal_params = SignalParameters(frequency=5e9, power=1, pulse_width=1e-6)
    antenna_params = AntennaParameters(gain_tx=30, gain_rx=30, beamwidth=3)
    scene = Scene()
    scene.add_object(SceneObject(position=[100, 0, 0], rcs=1.0))
    
    # Генерация сигнала
    signal_simulator = SignalSimulator(signal_params)
    t, pulse = signal_simulator.generate_pulse(duration=1e-6)
    
    # Распространение сигнала
    wave_propagator = WavePropagationSimulator(signal_params)
    propagated_pulse = wave_propagator.propagate(pulse, distance=100)
    
    # Отражение и прием сигнала
    reflection_calculator = ReflectionCalculator(scene)
    reflections = reflection_calculator.calculate_reflections(propagated_pulse, tx_position=np.array([0, 0, 0]))
    
    receiver_simulator = ReceiverSimulator(antenna_params)
    received_signal = receiver_simulator.receive(reflections)
    
    # Обработка сигнала
    signal_processor = SignalProcessingModule()
    compressed_signal = signal_processor.pulse_compression(received_signal, pulse)
    
    # Постобработка и визуализация
    post_processor = PostProcessingModule()
    filtered_signal = post_processor.noise_reduction(compressed_signal)
    post_processor.visualize(filtered_signal, title="Filtered Signal")
    
    # Верификация и отчетность
    verifier = VerificationModule()
    error = verifier.compare_with_real_data(filtered_signal,
                                            real_data=np.zeros_like(filtered_signal))  # Замените на реальные данные
    
    report_generator = ReportGenerator()
    report_generator.generate_report({"Error": error})


if __name__ == "__main__":
    main()
