/*
******************************************************************************
File:     main.c
Info:     Generated by Atollic TrueSTUDIO(R) 9.0.0   2019-11-06
*/
#include "stm32f4xx.h"
#include "FreeRTOS.h"
#include "task.h"
#include "GPIODriver.h"
#include "queue.h"
#include "semphr.h"


//Greed Led
#define LedGreen_port				    PORTD
#define	LedGreen_pin				    PIN12
GPIOcfgType LedGreen;
//Red diode
#define DiodeRed_port           PORTD
#define DiodeRed_pin            PIN14
GPIOcfgType DiodeRed;

uint32_t fjutek;
SemaphoreHandle_t xSemaphore = NULL;
SemaphoreHandle_t xMutex = NULL;
TaskHandle_t xLed1;
TaskHandle_t xLed2;

static void prvSetupHardware(void);
void vATaskFunction( void *pvParameters );
void vLedTask1( void *pvParameters );
void vLedTask2( void *pvParameters );

void vApplicationTickHook( void );


int main(void)
{
  int i = 0;

	// Hardware configuration
	prvSetupHardware();

	xSemaphore = xSemaphoreCreateBinary();
	if( xSemaphore == NULL ) while(1);

	xMutex = xSemaphoreCreateMutex();

	xTaskCreate( vLedTask1, "LEDTask1", 100, NULL, 1, &xLed1 );
	xTaskCreate( vLedTask2, "LEDTask2", 100, NULL, 2, &xLed2 );

	// Start the scheduler
	vTaskStartScheduler(); // should never return

  /* Infinite loop */
  while (1)
  {
	i++;
  }
}



static void prvSetupHardware(void)
{
	LedGreen.mode 	= output;
	LedGreen.pin 	= LedGreen_pin;
	LedGreen.port 	= LedGreen_port;
	LedGreen.pull	= pullDown;
	LedGreen.typ	= pushPull;
	gpioCfg(&LedGreen);

	DiodeRed.mode     = output;
	DiodeRed.pin      = DiodeRed_pin;
	DiodeRed.port     = DiodeRed_port;
	DiodeRed.pull     = pullDown;
	DiodeRed.typ      = pushPull;
	DiodeRed.speed    = medium;
	gpioCfg(&DiodeRed);

}

void vLedTask1( void *pvParameters )
{
    for( ;; )
    {
    	if(xSemaphoreTake(xMutex, 1000/portTICK_RATE_MS) == pdTRUE)
    	{
			for(int a=0;a<1;a++)
			{
				gpioPinSetState(LedGreen_port, LedGreen_pin, 0);
				for(int a=0;a<100000;a++)
				{
					__asm__(" NOP");
				}
				gpioPinSetState(LedGreen_port, LedGreen_pin, 1);
				for(int a=0;a<100000;a++)
				{
					__asm__(" NOP");
				}
			}
	    	xSemaphoreGive(xMutex);
    	}
    }
    vTaskDelete( NULL );
}


void vLedTask2( void *pvParameters )
{
    for( ;; )
    {
    	if(xSemaphoreTake(xMutex, 1000/portTICK_RATE_MS) ==pdTRUE)
    	{
        	for(int a=0;a<8;a++)
        	{
        		gpioPinSetState(DiodeRed_port, DiodeRed_pin, 1);
        		for(int a=0;a<100000;a++)
        		{
        			__asm__(" NOP");
        		}
        		gpioPinSetState(DiodeRed_port, DiodeRed_pin, 0);
        		for(int a=0;a<100000;a++)
        		{
        			__asm__(" NOP");
        		}
        	}
        	xSemaphoreGive(xMutex);
        	vTaskDelay(1);
    	}
    }
    vTaskDelete( NULL );
}

void vApplicationTickHook( void )
{
	fjutek++;
	if(fjutek == (32000))
	{
		fjutek =0;
	}
}