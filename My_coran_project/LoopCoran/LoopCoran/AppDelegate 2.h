//
//  AppDelegate.h
//  LoopCoran
//
//  Created by Bah Amadou Oury on 15/08/2020.
//  Copyright © 2020 Bah Amadou Oury. All rights reserved.
//

#import <UIKit/UIKit.h>
#import <CoreData/CoreData.h>

@interface AppDelegate : UIResponder <UIApplicationDelegate>

@property (readonly, strong) NSPersistentCloudKitContainer *persistentContainer;

- (void)saveContext;


@end

